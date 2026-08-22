from db import PgManager
from autorepo import AutomobileRepository

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="1234",
    host="localhost",
)
auto_repo = AutomobileRepository(db_manager)
available = auto_repo.get_available()
print("Available car", available)

db_manager.close_connection()
