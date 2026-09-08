from db import get_session
from models import User

def print_cars_n_addresses(user_id, session = None):
    close_finishing = session is None
    if session is None:
        session = get_session()
    user = session.get(User, user_id)
    if user is None:
        print(f"User with id {user_id} not found.")
        if close_finishing:
            session.close()
        return
    print(f"User: {user.name} (ID: {user.id})")
    print(f" Cars ({len(user.autos)}):")
    if not user.autos:
        print("  (No cars affiliated)")
    for car in user.autos:
        print(" -", car)
    print(f" Addresses ({len(user.addresses)}): ")
    if not user.addresses:
        print(" (No addresses found)")
    for address in user.addresses:
        print(" -", address)

    
    if close_finishing:
        session.close()

if __name__ == "__main__":
    print_cars_n_addresses(1)



