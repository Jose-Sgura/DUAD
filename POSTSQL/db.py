import psycopg2


class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully")
    

    def create_connection(self, db_name, user , password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the DATABASE", error)
            return None

    def close_connection(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, *args, commit = True):
        self.cursor.execute(query, args)
        if commit:
            self.connection.commit()

        if self.cursor.description:
            results = self.cursor.fetchall()
            return results
        return None
    
    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()
