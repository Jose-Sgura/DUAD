from db import get_session
from models import User, Automobile
from sqlalchemy import func

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
    print(f" Cars ({len(user.cars)}):")
    if not user.cars:
        print("  (No cars affiliated)")
    for car in user.cars:
        print(" -", car)
    print(f" Addresses ({len(user.addresses)}): ")
    if not user.addresses:
        print(" (No addresses found)")
    for address in user.addresses:
        print(" -", address)

def print_user_with_more_than_n_cars(n = 1, session = None):
    close_finishing  = session is None
    if session is None:
        session = get_session()
    results = (
        session.query(User.name, func.count(Automobile.id).label("car_count"))
        .join(Automobile, Automobile.user_id == User.id)
        .group_by(User.id, User.name)
        .having(func.count(Automobile.id) > n)
        .all()
    )

    print(f"Users with more than {n} car(s): ")
    if not results:
        print(" (none found)")
    for name, car_count in results:
        print(f" -{name}: {car_count} cars")

    
    if close_finishing:
        session.close()

if __name__ == "__main__":
    print_cars_n_addresses(1)



