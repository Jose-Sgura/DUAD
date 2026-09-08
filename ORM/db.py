from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session

from models import Base

DATABASE_URL = "postgresql://postgres:tu_nueva_contraseña@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo = True)
SessionLocal = sessionmaker(bind = engine, autoflush = False, expire_on_commit= False)

def test_connection():
    try:
        connection = engine.connect()
        print("Connection successful!")
        connection.close()
        
        return True
    except Exception as e:
        print("Connection failed: ", e)
        return False

def verify_create_tables():
    inspector = inspect(engine)
    existing_tables = set(inspector.get_table_names())
    print("Verifying  tables ...")

    for table in Base.metadata.tables.keys():
        status = "exists" if table in existing_tables else "does not exist, it will be created"
        print (f" - {table}: {status}")

# create_all es idempotente: si ya existe una tabla, la ignora;
# si falta, la crea.
    Base.metadata.create_all(bind = engine)
    print("Tables all-set. \n")

def get_session():
    return SessionLocal()

if __name__ == "__main__":
    test_connection()
