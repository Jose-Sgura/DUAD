from db import PgManager
from rentrepo import RentalRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="1234",
    host="localhost",
)
user_id = int(input("Enter user ID: "))
auto_id = int(input("Enter automobile ID: "))

rental_repo = RentalRepository(db_manager)
rental_repo.create(user_id, auto_id)

db_manager.close_connection()