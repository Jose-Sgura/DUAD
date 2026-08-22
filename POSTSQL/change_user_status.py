from db import PgManager
from userrepo import UserRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="1234",
    host="localhost",
)
user_id = int(input("Enter user ID: "))
new_status = input("Enter new status (active/inactive): ")

user_repo = UserRepository(db_manager)
user_repo.update_status(user_id, new_status)

db_manager.close_connection()