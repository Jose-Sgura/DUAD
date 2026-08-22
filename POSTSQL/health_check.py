from db import PgManager

REQUIRED_TABLES = ["users", "automobile", "rent"]
SCHEMA = "lyfter_car_rental"

def check_tables_exist(db_manager):
    query = (
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = %s AND table_name = ANY(%s)"
    )
    results = db_manager.execute_query(query, SCHEMA, REQUIRED_TABLES)
    found = {row[0] for row in results}
    missing = [t for t in REQUIRED_TABLES if t not in found]
    return missing

def check_available_cars(db_manager):
    query = f"SELECT COUNT(*) FROM {SCHEMA}.automobile WHERE status = 'Available'"
    result = db_manager.execute_query(query)
    count = result[0][0]
    return count

def run_health_check():
    try:
        db_manager = PgManager(
            db_name="postgres",
            user="postgres",
            password="tu_nueva_contraseña",
            host="localhost",
        )
    except Exception as error:
        print("DB ERROR. It could not connect to the data base")
        print   (f"Detail {error}")
        return
    
    if not db_manager.connection:
        print("DB ERROR. It could not connect to the data base ")
        return
    missing= check_tables_exist(db_manager)
    if missing:
        print(f"DB ERROR. Missing tables_ {' , '.join(missing)}")
        db_manager.close_connection()
        return
    available_cars = check_available_cars(db_manager)
    if available_cars < 1:
        print("DB ERROR. There are not enable cars")
        db_manager.close_connection()
        return
    
    print("DB OK. System working as usual ")
    db_manager.close_connection()

if __name__ == "__main__":
    run_health_check()
    
