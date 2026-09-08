from db import PgManager
from userrepo import UserRepository
from autorepo import AutomobileRepository
from rentrepo import RentalRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="tu_nueva_contraseña",
    host="localhost",
)
user_repo = UserRepository(db_manager)
formatted_results = user_repo.get_all()
print("Formatted Users:", formatted_results)
automobile_repo = AutomobileRepository(db_manager)
formatted_automobiles = automobile_repo.get_all()
print("Formatted Automobiles:", formatted_automobiles)
rental_repo = RentalRepository(db_manager)
formatted_rentals = rental_repo.get_all()
print("Formatted Rentals:", formatted_rentals)

db_manager.close_connection()
