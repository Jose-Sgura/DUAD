from db import PgManager
from autorepo import AutomobileRepository


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="tu_nueva_contraseña",
    host="localhost",
)

brand = input("Enter brand: ")
model = input("Enter model: ")
manufacturing_year = input("Enter manufacturing year: ")

auto_repo = AutomobileRepository(db_manager)
auto_repo.add(brand, model, manufacturing_year)

db_manager.close_connection()
