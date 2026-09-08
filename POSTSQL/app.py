from flask import Flask, request, jsonify

from db import PgManager
from userrepo import UserRepository
from autorepo import AutomobileRepository
from rentrepo import RentalRepository

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="tu_nueva_contraseña",
    host="localhost",
)

user_repo = UserRepository(db_manager)
automobile_repo = AutomobileRepository(db_manager)
rental_repo = RentalRepository(db_manager)

#---creations
@app.route("/users", methods = ["POST"])
def create_user():
    data = request.get_json()
    new_id = user_repo.add(
        data.get("full_name"),
        data.get("email"),
        data.get("user_name"),
        data.get("password"),
        data.get("birth_date")
    )
    if new_id is False:
        return jsonify({"error": "Could not create user"}), 400
    return jsonify({"id": new_id}), 201
@app.route("/automobiles", methods = ["POST"])
def create_automobile():
    data = request.get_json()
    new_id = automobile_repo.add(
        data.get("brand"),
        data.get("model"),
        data.get("manufacturing_year"),
        data.get("status", "Available")
    )
    if new_id is False:
        return jsonify({"error": "Could not create automobile"}), 400
    return jsonify({"id": new_id}), 201

@app.route("/rent", methods = ["POST"])
def create_rental():
    data = request.get_json()
    new_id = rental_repo.create(
        data.get("user_id"),
        data.get("auto_id")
    )
    if new_id is False:
        return jsonify({"error": "Could not create rental"}), 400
    return jsonify({"id": new_id}),201

#---modifications
@app.route("/automobiles/<int:auto_id>/status", methods = ["PATCH"])
def change_automobile_status(auto_id):
    data = request.get_json()
    new_status = data.get("status")
    if not new_status:
        return jsonify({"error":"Missing 'status' field"}), 400
    ok = automobile_repo.update_status(auto_id, new_status)
    if not ok:
        return jsonify({"Error": "Could not update automobile status"}), 400
    return jsonify({"message":f"Automobile {auto_id} status updated to {new_status}"}), 200

@app.route("/users/<int:user_id>/status", methods = ["PATCH"])
def change_user_status(user_id):
    data = request.get_json()
    new_status = data.get("status")
    if not new_status:
        return jsonify({"Error": "Missing 'status' field"}), 400
    ok = user_repo.update_status(user_id, new_status)
    if not ok:
        return jsonify({"Error":"Could not update user status"}),400
    return jsonify({"message":f"User {user_id} status updated to '{new_status}'"}), 200

@app.route("/rent/<int:rental_id>/complete", methods = ["PATCH"])
def complete_rental(rental_id):
    ok = rental_repo.complete_return(rental_id)
    if not ok:
        return jsonify({"error":"Could not complete rental"}), 400
    return jsonify({"message":f"Rental {rental_id} completed"}), 200

@app.route("/rent/<int:rental_id>/delinquent", methods = ["PATCH"])
def change_rental_status(rental_id):
    data = request.get_json()
    new_status = data.get("status")
    if not new_status:
        return jsonify({"error":"Missing 'status' field"}),400
    ok = rental_repo.update_status(rental_id, new_status)
    if not ok:
        return jsonify({"error":"Could not update rental status"}),400
    return jsonify({"message":f"Rental{rental_id} status updated to '{new_status}'"}),200

@app.route("/users/<int:user_id>/delinquent", methods = ["PATCH"])
def flag_user_delinquent(user_id):
    data = request.get_json(silent= True) or {}
    is_delinquent = data.get("is_delinquent", True)
    ok = user_repo.set_delinquent(user_id, is_delinquent)
    if not ok:
        return jsonify({"error":"Could not update delinquent flag"}),400
    return jsonify({"message": f"User {user_id} delinquent flag set to {is_delinquent}"}), 200

#----listas
@app.route("/users", methods = ["GET"])
def list_users():
    filters = request.args.to_dict()
    results = user_repo.get_all(filters=filters)
    if results is False:
        return jsonify({"error":"Could not fetch users"}), 400
    return jsonify (results),200
@app.route("/automobiles", methods = ["GET"])
def list_automobile():
    filters = request.args.to_dict()
    results = automobile_repo.get_all(filters=filters)
    if results is False:
        return jsonify({"error" : "Could not fetch automobile"}),400
    return jsonify(results),200
@app.route("/rent", methods = ["GET"])
def list_rents():
    filters = request.args.to_dict()
    results = rental_repo.get_all(filters = filters)
    if results is False:
        return jsonify({"error": "Could not fetch rentals"}), 400
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)



