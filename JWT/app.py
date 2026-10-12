import datetime
import os
from dotenv import load_dotenv

load_dotenv()
import jwt as pyjwt
from flask import Flask, g, jsonify, request
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError


from auth import login_required
from db import DB_Manager
from JWT_Manager import JWT_Manager

app = Flask("fruit-store")
db_manager = DB_Manager()
ph= PasswordHasher()

KEYS_DIR = os.environ.get("JWT_KEYS_DIR", os.path.join(os.path.dirname(__file__), "keys"))
with open(os.path.join(KEYS_DIR, "private.pem"), "rb") as f:
    PRIVATE_KEY = f.read()
with open(os.path.join(KEYS_DIR,"public.pem"), "rb") as f:
    PUBLIC_KEY = f.read() 

jwt_manager = JWT_Manager(PRIVATE_KEY, PUBLIC_KEY, "RS256")

app.config["DB_MANAGER"] = db_manager
app.config["JWT_MANAGER"] = jwt_manager

VALID_ROLES = {"admin", "user"}

ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)

def _issue_tokens(user_id, role):
    access = jwt_manager.encode({"id": user_id, "role": role, "type": "access"}, ACCESS_TOKEN_EXPIRES)
    refresh = jwt_manager.encode({"id": user_id, "role": role, "type": "refresh"}, REFRESH_TOKEN_EXPIRES)
    if access is None or refresh is None:
        return None
    return {"token": access, "refresh_token": refresh}

def _record_login(user_id, username, success):
    try:
        db_manager.insert_login_history(user_id, username, request.remote_addr or "unknown", success)
    except Exception:
        pass

@app.route("/liveness")
def liveness():
    return "<p> Hello, World!</p>"

#----------------
#AUTH
#--------------

@app.route("/register", methods = ["POST"])
def register():
    
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error = "Request body must be JSON"), 400
    
    username = data.get("username")
    password = data.get("password")
    requested_role = data.get("role", "user")

    if not username or not password:
        return jsonify(error= "username and password are required"), 400
    if requested_role not in VALID_ROLES:
        return jsonify(error= f"role must be one of  {sorted(VALID_ROLES)}"), 400
    if requested_role == "admin":
        try:
            existing_admins = db_manager.count_admins()
        except Exception:
            return jsonify(error = "internal server error"), 500
        if existing_admins > 0:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return jsonify(error = "Only an admin can create another admin"), 403
        
            token= auth_header.replace("Bearer ", "",1)
            try:
                decoded = jwt_manager.decode(token)
            except Exception:
                return jsonify(error = "Invalid or expired token"), 401
            if not decoded or decoded.get("type") != "access":
                return jsonify(error = "Invalid or expired token"),401
        
            requester = db_manager.get_user_by_id(decoded.get("id"))
            if not requester or requester.role!= "admin":
                return jsonify(error="Only an admin can create another admin"), 403
    try:
        existing = db_manager.get_user_by_username(username)
        if existing is not None:
            return jsonify(error= "Username is taken"), 409

        password_hash = ph.hash(password)
        new_user = db_manager.insert_user(username, password_hash, requested_role)
        user_id = new_user[0]

        tokens = _issue_tokens(user_id, requested_role)
        if tokens is None:
            return jsonify(error = "Internal server error"), 500
        
        return jsonify(**tokens), 201
    except Exception:
        return jsonify(error = "Internal server error"), 500
    
@app.route("/login", methods =["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error="Request body must be JSON"), 400
    username= data.get("username")
    password=data.get("password")

    if not username or not password:
        return jsonify(error= "username and password are required"), 400
    try:
        user = db_manager.get_user_by_username(username)
    except Exception:
        return jsonify(error ="Internal server error"), 500
    if user is None:
        _record_login(None, username, False)
        return jsonify(error="Invalid credentials"), 401
    try:
        ph.verify(user.password, password)
    except (VerifyMismatchError, InvalidHashError):
        _record_login(user.id, username, False)
        return jsonify(error="Invalid credentials"), 401
    
    tokens = _issue_tokens(user.id, user.role)
    if tokens is None:
        return jsonify(error = "Internal server error"),500
    
    _record_login(user.id, username, True)
    return jsonify(**tokens), 200

@app.route("/refresh-token", methods=["POST"])
def refresh_token():
    data = request.get_json(silent=True) or {}
    token = data.get("refresh_token")
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header:
            token = auth_header.replace("Bearer ", "", 1)
    if not token:
        return jsonify(error = "refresh_token is required"), 400
    try:
        decoded = jwt_manager.decode(token)
    except pyjwt.ExpiredSignatureError:
        return jsonify(error = "Refresh token has expired"), 401
    except pyjwt.InvalidTokenError:
        return jsonify(error = "Invalid token"), 401
    except Exception:
        return jsonify(error = "Internal server error"), 500
    if not decoded or decoded.get("type") != "refresh" or "id" not in decoded:
        return jsonify(error = "Invalid token"), 401
        
    try:
        user = db_manager.get_user_by_id(decoded["id"])
    except Exception:
        return jsonify(error = "Internal server error"), 500
    if user is None:
        return jsonify(error = "Invalid token"), 401
    new_access = jwt_manager.encode({"id": user.id, "role": user.role, "type": "access"}, ACCESS_TOKEN_EXPIRES)
    if new_access is None:
        return jsonify(error = "Internal server error"), 500
    return jsonify(token=new_access), 200
@app.route("/login-history", methods =["GET"])
@login_required(roles=["admin"])
def login_history():
    user_id = request.args.get("user_id")
    username = request.args.get("username")
    if user_id is not None:
        try:
            user_id = int(user_id)
        except ValueError:
            return jsonify(error = "user_id must be an integer"), 400
    try:
        rows = db_manager.get_login_history(user_id = user_id, username = username)
        return jsonify([{
            "id": r.id,
            "user_id": r.user_id,
            "username": r.username,
            "login_date": r.login_date.isoformat(),
            "ip_address": r.ip_address,
            "success": r.success,
        }
        for r in rows]), 200
    except Exception:
        return jsonify(error = "Internal server error"), 500
    

@app.route("/me")
@login_required()
def me():
    return jsonify(id=g.user_id, username=g.username, role=g.role), 200

# ------------------------ #
# Products (CRUD, solo administrador)
# -----------------------#
def _serialize_product(p):
    return{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "entry_date": p.entry_date.isoformat(),
        "quantity": p.quantity,
    }

@app.route("/products", methods=["POST"])
@login_required(roles=["admin"])
def create_product():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error = "Request body must be JSON"),400
    name = data.get("name")
    price = data.get("price")
    entry_date = data.get("entry_date")
    quantity = data.get("quantity")
    if name is None or price is None or entry_date is None or quantity is None:
        return jsonify(error="name, price, entry_date and quantity are required"), 400
    
    try:
        price = float(price)
        quantity = int(quantity)
        entry_date_parsed = datetime.date.fromisoformat(entry_date)
    except (ValueError, TypeError):
        return jsonify(error = "Invalid field types (price: number, quantity: int, entry_date: YYYY-MM-DD)"),400
    if price < 0 or quantity < 0:
        return jsonify(error = "price and quantity must not be negative"), 400
    try:
        new_id = db_manager.create_product(name, price, entry_date_parsed, quantity)[0]
        product = db_manager.get_product_by_id(new_id)
        return jsonify(_serialize_product(product)),201
    except Exception:
        return jsonify(error = "Internal server error"), 500
@app.route("/products", methods = ["GET"])
@login_required(roles=["admin"])
def list_products():
    try:
        products = db_manager.get_products()
        return jsonify([_serialize_product(p) for p in products]),200
    except Exception:
        return jsonify(error="Internal server error"),500
    
@app.route("/products/<int:product_id>", methods = ["GET"])
@login_required(roles=["admin"])
def get_product(product_id):
    try:
        product = db_manager.get_product_by_id(product_id)
    except Exception:
        return jsonify(error = "Internal server error"), 500
    if product is None:
        return jsonify(error="Product not found"), 404
    
    return jsonify(_serialize_product(product)), 200

@app.route("/products/<int:product_id>", methods = ["PUT"])
@login_required(roles=["admin"])
def update_product(product_id):
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error = "Request body must be JSON"), 400
    try:
        existing = db_manager.get_product_by_id(product_id)
    except Exception:
        return jsonify(error = "Internal server error"),500
    if existing is None:
        return jsonify(error="Product not found"), 404
    
    fields = {}

    try:
        if "name" in data:
            fields["name"] = data["name"]
        if "price" in data:
            fields["price"] = float(data["price"])
        if "quantity" in data:
            fields["quantity"] = int(data["quantity"])
        if "entry_date" in data:
            fields["entry_date"] = datetime.date.fromisoformat(data["entry_date"])
    except (ValueError, TypeError):
        return jsonify(error = "Invalid field types"), 400
    if fields.get("price", 0)< 0 or fields.get("quantity", 0) < 0:
        return jsonify(error = "price and quantity must not be negative"), 400
    
    try:
        updated = db_manager.update_product(product_id, **fields)
        return jsonify(_serialize_product(updated)),200
    except Exception:
        return jsonify(error = "Internal server error"), 500
    
@app.route("/products/<int:product_id>", methods = ["DELETE"])
@login_required(roles=["admin"])
def delete_product(product_id):
    try:
        existing = db_manager.get_product_by_id(product_id)
        if existing is None:
            return jsonify(error = "Product not found"), 404
        db_manager.delete_product(product_id)
        return "", 204
    except Exception:
        return jsonify(error = "Internal server error"), 500
    

#---------------#
#Sales / Invoice (admin y user)
#---------------#
@app.route("/purchase", methods = ["POST"])
@login_required(roles=["admin", "user"])
def purchase():
    data=request.get_json(silent=True)
    if not data or "items" not in data:
        return jsonify(error = "items is required, e.g. {\"items\": [{\"product_id\": 1, \"quantity\": 2}]}"), 400
    items = data["items"]
    if not isinstance(items,list) or len(items) == 0:
        return jsonify(error = "items must be a non-empty list"),400
    parsed_items = []

    for item in items:
        if not isinstance(item, dict):
            return jsonify(error = "each item must be an object with product_id and quantity"), 400
        product_id = item.get("product_id")
        quantity = item.get("quantity")
        if product_id is None or quantity is None:
            return jsonify(error="each item requires product_id and quantity"),400
        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except (ValueError, TypeError):
            return jsonify(error = "product_id and quantity must be integers"),400
        if quantity <= 0:
            return jsonify(error = "quantity must be greater than 0"), 400
        
        parsed_items.append({"product_id": product_id, "quantity": quantity})

    try:
        invoice = db_manager.create_invoice_with_items(g.user_id, parsed_items)
        return(
            jsonify(
                id=invoice["id"],
                total=invoice["total"],
                items =[
                    {
                        "product_id": it["product_id"],
                        "quantity": it["quantity"],
                        "unit_price": it["unit_price"],
                    }
                    for it in invoice["items"]
                ],
            ),
            201,
        )
        
    except ValueError as ve:
        return jsonify(error= str(ve)), 400
    except Exception:
        return jsonify(error= "Internal server error"), 500

@app.route("/invoices", methods =["GET"])
@login_required(roles=["admin", "user"])
def list_invoice():
    try:
        invoices = db_manager.get_invoices_by_user(g.user_id)
        return (
            jsonify(
                [
                    {
                        "id":entry["invoice"].id,
                        "date": entry["invoice"].date.isoformat(),
                        "total": entry["invoice"].total,
                        "items":[
                        {
                            "product_id": it.product_id,
                            "quantity": it.quantity,
                            "unit_price": it.unit_price,
                        }
                        for it in entry["items"]
                        ],
                    }
                    for entry in invoices
                ]
            ), 
            200,
        )
    except Exception:
        return jsonify(error="Internal server error"), 500
    
# Agenda de contactos
#  - user: solo ve/gestiona SUS contactos
#  - admin: ve TODOS y puede eliminar cualquiera; crear/editar solo los suyos
def _serialize_contact(c):
    return {
        "id": c.id,
        "user_id": c.user_id,
        "name": c.name,
        "phone": c.phone,
        "email": c.email,
    }
def _clean_str(value):
    if not isinstance(value,str) or not value.strip():
        return None
    return value.strip()

@app.route("/contacts", methods = ["POST"])
@login_required(roles=["admin", "user"])
def create_contact():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error = "Request body must be JSON"), 400
    name = _clean_str(data.get("name"))
    phone = _clean_str(data.get("phone"))
    email = _clean_str(data.get("email"))
    if not name or not phone or not email:
        return jsonify(error = "name, phone and email are required (non-empty strings)"), 400
    if "@" not in email:
        return jsonify(error = "email must be a valid email address"), 400
    try:
        new_id = db_manager.create_contact(g.user_id, name, phone, email)[0]
        return jsonify(_serialize_contact(db_manager.get_contact_by_id(new_id))), 201
    except Exception:
        return jsonify(error = "Internal server error"), 500
@app.route("/contacts", methods = ["GET"])
@login_required(roles=["admin", "user"])
def list_contacts():
    try:
        owner = None if g.role == "admin" else g.user_id
        contacts = db_manager.get_contacts(user_id = owner)
        return jsonify([_serialize_contact(c) for c in contacts]), 200
    except Exception:
        return jsonify(error = "Internal server error"), 500

@app.route("/contacts/<int:contact_id>", methods = ["GET"])
@login_required(roles=["admin", "user"])
def get_contact(contact_id):
    try:
        contact = db_manager.get_contact_by_id(contact_id)
    except Exception:
        return jsonify(error = "Internal server error"), 500
    if contact is None or (g.role != "admin" and contact.user_id != g.user_id):
        return jsonify(error = "Contact not found"), 404
    return jsonify(_serialize_contact(contact)), 200
@app.route("/contacts/<int:contact_id>", methods = ["PUT"])
@login_required(roles=["admin", "user"])
def update_contact(contact_id):
    data = request.get_json(silent = True)
    if not data:
        return jsonify(error = "Request body must be JSON"), 400
    try:
        contact = db_manager.get_contact_by_id(contact_id)
    except Exception:
        return jsonify(error = "Internal server error"), 500
    if contact is None:
        return jsonify(error = "Contact not found"), 404
    if contact.user_id != g.user_id:
        if g.role == "admin":
            return jsonify(error = "Admins can only update their own contacts"), 403
        return jsonify(error = "Contact not found"), 404
    fields = {}
    for key in ("name", "phone", "email"):
        if key in data:
            value = _clean_str(data[key])
            if value is None:
                return jsonify(error = f"{key} must be a non-empty string"), 400
            fields[key] = value
    if "email" in fields and "@" not in fields["email"]:
        return jsonify(error = "email must be a valid email address"), 400
    if not fields:
        return jsonify(error = "Nothing to update (name, phone or email)"), 400
    
    try:
        updated = db_manager.update_contact(contact_id, **fields)
        return jsonify(_serialize_contact(updated)), 200
    except Exception:
        return jsonify(error = "Internal server error"), 500
    
@app.route("/contacts/<int:contact_id>", methods = ["DELETE"])
@login_required(roles=["admin", "user"])
def delete_contact(contact_id):
    try:
        contact = db_manager.get_contact_by_id(contact_id)
        if contact is None or (g.role != "admin" and contact.user_id != g.user_id):
            return jsonify(error = "Contact not found"), 404
        db_manager.delete_contact(contact_id)
        return "", 204
    except Exception:
        return jsonify(error = "Internal server error"), 500
@app.errorhandler(404)
def not_found(_e):
    return jsonify(error = "Not found"), 404

@app.errorhandler(405)
def method_not_allowed(_e):
    return jsonify(error="Method not allowed"), 405

if __name__ == "__main__":
    app.run(debug=True)