import os 

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float, Date, DateTime, Boolean, ForeignKey
from sqlalchemy import insert, select, update, delete
from datetime import datetime,timezone

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30), unique=True, nullable=False),
    Column("password", String, nullable=False),
    Column("role", String(20), nullable=False, default="user"),
)

product_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("price", Float, nullable = False),
    Column("entry_date", Date, nullable = False),
    Column("quantity", Integer, nullable = False),
)

invoice_table = Table(
    "invoices",
    metadata_obj,
    Column("id", Integer, primary_key = True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable = False),
    Column("date", DateTime, nullable = False),
    Column("total", Float, nullable=False)
)

invoice_item_table = Table(
    "invoice_items",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("invoice_id", Integer, ForeignKey("invoices.id"), nullable=False),
    Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("unit_price", Float, nullable=False),
)
contact_table = Table(
    "contacts",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer,ForeignKey("users.id"), nullable=False),
    Column("name", String(100), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("email", String(100), nullable=False),
)

login_history_table = Table(
    "login_history",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=True),
    Column("username", String(100), nullable=False),
    Column("login_date", DateTime, nullable=False),
    Column("ip_address", String(45), nullable=False),
    Column("success", Boolean, nullable=False),
)

class DBManager:
    def __init__(self, connection_string=None):
        connection_string = connection_string or os.environ.get(
            "DATABASE_URL",
            "postgresql+psycopg2://postgres:FrutasTienda123@localhost:5432/postgres",

        )
        self.engine = create_engine(connection_string)
        metadata_obj.create_all(self.engine)
    
    
    #users
    def insert_user(self, username, password_hash, role="user"):
        stmt = (
            insert(user_table)
            .returning(user_table.c.id)
            .values(username=username, password=password_hash, role=role)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.all()
            conn.commit()
            return rows[0] if rows else None
    
    def get_user_by_username(self, username):
        stmt = select(user_table).where(user_table.c.username == username)
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
            return rows[0] if rows else None
    
    def get_user_by_id(self, user_id):
        stmt = select(user_table).where(user_table.c.id == user_id)
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
            return rows[0] if rows else None
    def count_admins(self):
        stmt = select(user_table).where(user_table.c.role == "admin")
        with self.engine.connect() as conn:
            return len(conn.execute(stmt).all())
#products

    def create_product(self, name, price, entry_date, quantity):
        stmt = (
            insert(product_table)
            .returning(product_table.c.id)
            .values(name = name, price = price, entry_date = entry_date, quantity = quantity)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.all()
            conn.commit()
            return rows[0]
    def get_products(self):
        stmt = select(product_table)
        with self.engine.connect() as conn:
            return conn.execute(stmt).all()
    def get_product_by_id(self, product_id):
        stmt = select(product_table).where(product_table.c.id == product_id)
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
            return rows[0] if rows else None
    def update_product(self, product_id, **fields):
        fields = {k: v for k, v in fields.items() if v is not None}
        if not fields:
            return self.get_product_by_id(product_id)
        stmt = update(product_table).where(product_table.c.id == product_id).values(**fields)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return self.get_product_by_id(product_id)
    def delete_product(self, product_id):
        stmt = delete(product_table).where(product_table.c.id == product_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount > 0
    #ventas / facturas
    def create_invoice_with_items(self, user_id, items):
        with self.engine.connect() as conn:
            total = 0.0
            resolved_items = []

            for item in items:
                product_id = item["product_id"]
                qty = item["quantity"]

                stmt = select(product_table).where(product_table.c.id == product_id)
                rows = conn.execute(stmt).all()
                if not rows:
                    raise ValueError(f"Product {product_id} not found")
                product = rows[0]
                if product.quantity < qty:
                    raise ValueError(f"Not enough stock for product '{product.name}'")
                unit_price = product.price
                total += unit_price * qty
                resolved_items.append({
                    "product_id": product_id,
                    "quantity": qty,
                    "unit_price": unit_price,
                    "new_quantity": product.quantity - qty,

                }
                )
            invoice_stmt = (
                insert(invoice_table)
                .returning(invoice_table.c.id)
                .values(user_id = user_id, date= datetime.now(timezone.utc), total = total)
            )
            invoice_id = conn.execute(invoice_stmt).all()[0][0]

            for ri in resolved_items:
                conn.execute(
                    insert(invoice_item_table).values(
                        invoice_id = invoice_id,
                        product_id = ri["product_id"],
                        quantity = ri["quantity"],
                        unit_price = ri["unit_price"],
                    )
                )
                conn.execute(
                    update(product_table)
                    .where(product_table.c.id == ri["product_id"])
                    .values(quantity = ri["new_quantity"])
                )
            conn.commit()
            return{"id": invoice_id, "total": total, "items": resolved_items}
    def get_invoices_by_user(self, user_id):
        invoices_stmt = select(invoice_table).where(invoice_table.c.user_id == user_id).order_by(invoice_table.c.id)
        with self.engine.connect() as conn:
            invoices = conn.execute(invoices_stmt).all()
            if not invoices:
                return []
            invoice_ids = [inv.id for inv in invoices]
            items_stmt = select(invoice_item_table).where(invoice_item_table.c.invoice_id.in_(invoice_ids)).order_by(invoice_item_table.c.id)
            items = conn.execute(items_stmt).all()

        items_by_invoice = {}
        for item in items:
            items_by_invoice.setdefault(item.invoice_id, []).append(item)
        return [
            {"invoice": inv, "items": items_by_invoice.get(inv.id, [])}
            for inv in invoices
        ]

    def create_contact(self, user_id, name, phone, email):
        stmt = (
            insert(contact_table)
            .returning(contact_table.c.id)
            .values(user_id = user_id, name = name, phone = phone, email = email)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.all()
            conn.commit()
            return rows[0]
    def get_contacts(self, user_id = None):
        stmt = select(contact_table).order_by(contact_table.c.id)
        if user_id is not None:
            stmt = stmt.where(contact_table.c.user_id == user_id)
        with self.engine.connect() as conn:
            return conn.execute(stmt).all()
    def get_contact_by_id(self, contact_id):
        stmt = select(contact_table).where(contact_table.c.id == contact_id)
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
            return rows[0] if rows else None
    def update_contact(self, contact_id, **fields):
        fields = {k: v for k, v in fields.items() if v is not None}
        if not fields:
            return self.get_contact_by_id(contact_id)
        stmt = update(contact_table).where(contact_table.c.id == contact_id).values(**fields)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return self.get_contact_by_id(contact_id)
    def delete_contact(self, contact_id):
        stmt = delete(contact_table).where(contact_table.c.id == contact_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount > 0
    def insert_login_history(self, user_id, username,ip_address, success):
        stmt = insert(login_history_table).values(
            user_id = user_id,
            username = username,
            login_date = datetime.now(timezone.utc),
            ip_address = ip_address,
            success = success

            )
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
    def get_login_history(self, user_id  = None, username = None):
        stmt = select(login_history_table).order_by(login_history_table.c.login_date.desc(), login_history_table.c.id.desc())
        if user_id is not None:
            stmt = stmt.where(login_history_table.c.user_id == user_id)
        if username is not None:
            stmt = stmt.where(login_history_table.c.username == username)
        with self.engine.connect() as conn:
            return conn.execute(stmt).all()