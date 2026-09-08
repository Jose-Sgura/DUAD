from db import PgManager
from userrepo import UserRepository

db_manager = PgManager(
    db_name="postgres", 
    user="postgres",
    password="1234",
    host="localhost",
)
full_name = input("Enter full name: ")
email = input("Enter email:")
user_name = input("Enter user name:")
password = input("Enter password:")
birth_date = input("Enter birth date (YYYY-MM-DD):")

user_repo = UserRepository(db_manager)
user_repo.add(full_name, email, user_name, password, birth_date)

db_manager.close_connection()