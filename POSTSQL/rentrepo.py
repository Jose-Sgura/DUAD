class RentalRepository:
    ALLOWED_FILTERS = {"id", "user_id", "auto_id", "rental_date", "status"}

    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_rental(self, rental_record):
        return {    
            "id": rental_record[0],
            "user_id": rental_record[1],
            "auto_id": rental_record[2],
            "rental_date": rental_record[3],
            "status": rental_record[4],
        }
    def get_all(self, filters = None):
        try:
            query= "SELECT id, user_id, auto_id, rental_date, status FROM lyfter_car_rental.rent"
            params = []
            valid_filter = {k : v for k , v in (filters or {}).items() if k in self.ALLOWED_FILTERS}
            if valid_filter:
                conditions = [f"{column} = %s" for column in valid_filter]
                query+= " WHERE " + " AND ".join(conditions)
                params = list(valid_filter.values())
            query += ";"
            results = self.db_manager.execute_query(query, *params)
            return [self._format_rental(result) for result in results]
        except Exception as error:
            self.db_manager.rollback()
            print("Error fetching rentals", error)
            return False
        #Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
    def create(self, user_id, auto_id):
        try:
            result = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rent(user_id, auto_id, status)" 
                "VALUES (%s, %s, 'Active') RETURNING id;",
                user_id, auto_id,
                commit = False
            )
            rental_id = result[0][0]

            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.automobile SET status = 'Rented' WHERE id = %s;",
                auto_id,
                commit = False
            )
            self.db_manager.commit()
            print(f"Rental created with the ID: {rental_id}")
            return rental_id
        except Exception as error:
            self.db_manager.rollback()
            print("Error creating rental:", error)
            return False
        
    def update_status(self, rental_id, new_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rent SET status = %s WHERE id = %s",
                new_status, rental_id
            )
            print(f"Rental {rental_id} status updated to '{new_status}' ")
            return True
        except Exception as error:
            self.db_manager.rollback()
            print("Error updating rental satus", error)
            return False
        
        
        #Un script que confirme la devolución del auto al completar el alquiler, c
        # olocando el auto como disponible y completando el estado del alquiler 
    def complete_return(self, rental_id):
        try:
            rental_row = self.db_manager.execute_query(
                "SELECT auto_id FROM lyfter_car_rental.rent WHERE id = %s;",
                rental_id,
                commit = False)
            if not rental_row:
                print(f"Rental{rental_id} not found.")
                return False
            auto_id = rental_row[0][0]

            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rent SET status = 'Completed' WHERE id = %s;",
                rental_id,
                commit = False
            )
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.automobile SET status = 'Available' WHERE id = %s;",
                auto_id,
                commit = False
            )
            self.db_manager.commit()
            print(f"Rental {rental_id} completed, automobile {auto_id} is now available.")
            return True

        except Exception as error:
            self.db_manager.rollback()
            print("Error completing rental return:", error)
            return False
