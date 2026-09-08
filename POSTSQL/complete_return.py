from db import PgManager
from rentrepo import RentalRepository

db_manager = PgManager(
    db_name= "postgres",
    user="postgres",
    password="1234",
    host="localhost",
    )
rental_id = int(input("Rental id: "))

rental_repo = RentalRepository(db_manager)
rental_repo.complete_return(rental_id)


db_manager.close_connection()
