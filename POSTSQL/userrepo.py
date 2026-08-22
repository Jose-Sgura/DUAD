class UserRepository:
    ALLOWED_FILTERS = {"id", "full_name", "email", "user_name", "birth_date", "status","is_delinquent"}

    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "user_name": user_record[3],
            "password": user_record[4],
            "birth_date": user_record[5],
            "status": user_record[6],
            "is_delinquent": user_record[7]
        }
    def get_all(self, filters = None):
        try:
            query = (
                "SELECT id, full_name, email, user_name, password, birth_date, status, is_delinquent " 
                "FROM lyfter_car_rental.users"
            )
            params = []
            valid_filters = {k: v for k, v in (filters or {}).items() if k in self.ALLOWED_FILTERS}
            if valid_filters:
                conditions = [f"{column} = %s" for column in valid_filters]
                query+= " WHERE " + " AND ".join(conditions)
                params = list(valid_filters.values())
            query+=";"
            results = self.db_manager.execute_query(query, *params)
            return [self._format_user(result) for result in results]
        except Exception as error:
            self.db_manager.rollback()
            print("Error fetching users:", error)
            return False

        #1.Un script que agregue un usuario nuevo
    def add(self, full_name, email, user_name, password, birth_date):
        try:
            result = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users" 
                "(full_name, email, user_name, password, birth_date)" 
                "VALUES (%s, %s, %s, %s, %s) RETURNING id;",
                full_name, email, user_name, password, birth_date
                )
            new_id = result[0][0]
            print(f"User created with the ID: {new_id}")
            return new_id
        except Exception as error:
            self.db_manager.rollback()
            print("Error adding user:", error)
            return False
        #3.Un script que cambie el estado de un usuario
    def update_status(self, user_id, new_status):
        try:
            result = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET status = %s WHERE id = %s;",
                new_status, user_id
            )
            print(f"User {user_id} status updated to {new_status}")
            return True
        except Exception as error:
            self.db_manager.rollback()
            print("Error updating user status:", error)
            return False
        
    def set_delinquent(self,user_id, is_delinquent=True):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET is_delinquent = %s WHERE id = %s",
                is_delinquent, user_id
            )
            print(f"User {user_id} delinquent flag set to {is_delinquent}")
            return True
        except Exception as error:
            self.db_manager.rollback()
            print("Error flagging  user as delinquent", error)
            return False
        