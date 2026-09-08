class AutomobileRepository:
    ALLOWED_FILTERS = {"id","brand","model", "manufacturing_year","status"}

    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_automobile(self, automobile_record):
        return {
            "id": automobile_record[0],
            "brand": automobile_record[1],
            "model": automobile_record[2],
            "manufacturing_year": automobile_record[3],
            "status": automobile_record[4],
        }
    def get_all(self,filters = None):
        try:
            query = "SELECT id, brand, model, manufacturing_year, status FROM lyfter_car_rental.automobile"
            params = []
            valid_filters = {k : v for k, v in (filters or {}).items() if k in self.ALLOWED_FILTERS}
            if valid_filters:
                conditions = [f"{column} = %s" for column in valid_filters]
                query+= " WHERE " + " AND ".join(conditions)
                params = list(valid_filters.values())
            query+= ";"
            results = self.db_manager.execute_query(query, *params)
            return [self._format_automobile(result) for result in results]
        except Exception as error:
            self.db_manager.rollback()
            print("Error fetching cars", error)
            return False


        #Un script que agregue un automovil nuevo
    def add(self, brand, model, manufacturing_year, status = "Available"):
        try:
            result = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.automobile"
                "(brand, model, manufacturing_year, status)"
                "VALUES(%s, %s, %s,%s) RETURNING id;",
                brand, model, manufacturing_year, status
                )
            new_id = result[0][0]
            print(f"Automobile created with the ID: {new_id}")
            return new_id
        except Exception as error:
            self.db_manager.rollback()
            print("Error adding automobile:", error)
            return False
        
        #un script que cambie el estado de un automovil
    def update_status(self,auto_id, new_status):
        try:
            result = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.automobile SET status = %s WHERE id = %s;",
                new_status, auto_id
            )
            print(f"Automobile {auto_id} status updated to {new_status}")
            return True
        except Exception as error:
            self.db_manager.rollback()
            print("Error updating automobile status:", error)
            return False
    
    def get_by_status(self,status):
        return self.get_all(filters={"status" : status})
    def get_rented(self):
        return self.get_by_status("Rented")
    def get_available(self):
        return self.get_by_status("Available")