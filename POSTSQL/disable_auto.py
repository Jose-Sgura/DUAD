from db import PgManager
from autorepo import AutomobileRepository

db_manager = PgManager(
    db_name= "postgres",
    user="postgres",
    password="1234",
    host="localhost"
)

auto_id = int(input("Enter auto id to disable: "))

auto_repo = AutomobileRepository(db_manager)
auto_repo.update_status(auto_id, "Disabled")

db_manager.close_connection()
