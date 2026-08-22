import csv
import os
from datetime import date

from db import PgManager

TABLES  = ["users", "automobile", "rent"]
SCHEMA = "lyfter_car_rental"

BACKUP_FOLDER = "db_backups"

def backup_table(db_manager, table_name, today_str):
    query = f"SELECT * FROM {SCHEMA}.{table_name};"
    rows = db_manager.execute_query(query)

    column_names = [col.name for col in db_manager.cursor.description]

    file_path = os.path.join(BACKUP_FOLDER, f"{table_name}_{today_str}.csv")

    with open(file_path, mode = "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)
    
    print({f"Backup of {table_name} saved in: {file_path}({len(rows)} rows)"})

def run_backup():
    os.makedirs(BACKUP_FOLDER, exist_ok = True)

    db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="tu_nueva_contraseña",
        host="localhost",
    )

    today_str = date.today().isoformat()

    for table_name in TABLES:
        backup_table(db_manager, table_name, today_str)
    
    db_manager.close_connection()

if __name__ == "__main__":
    run_backup()

