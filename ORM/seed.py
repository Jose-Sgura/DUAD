import random
from faker import Faker
from db import verify_create_tables, get_session
from manager import User_Manager, Automobile_Manager, Address_Manager

fake = Faker("en_US")

MODEL_BRANDS = [
    ("Toyota", "Corolla"),
    ("Honda", "Civic"),
    ("Mazda", "3"),
    ("Chevrolet", "Spark"),
    ("Nissan", "Sentra"),
    ("Kia", "Rio"),
    ("Hyundai", "Accent"),
    ("Ford", "Fiesta"),
]

def generate_plate():
    return fake.unique.bothify(text = '???-###').upper()

def populate(user_amount = 20, car_withno_owner = 5):
    verify_create_tables()
    session = get_session()
    users = User_Manager(session)
    cars = Automobile_Manager(session)
    addresses = Address_Manager(session)

    for _ in range(user_amount):
        user = users.create_user(
            name = fake.name(),
            email = fake.unique.email(),
            phone = fake.msisdn()[:20], 
        )
        for _ in range(random.randint(1, 2)):
            addresses.create_address(
                street = fake.street_address()[:150],
                city = fake.city()[:80],
                zip_code = fake.postcode()[:15],
                user_id = user.id,

            )
        for _ in range(random.randint(0,2)):
            brand, model = random.choice(MODEL_BRANDS)
            cars.create_automobile(
                brand = brand,
                model = model,
                plate = generate_plate(),
                year = random.randint(2005, 2025),
                user_id = user.id
            )
        
    for _ in range(car_withno_owner):
        brand, model = random.choice(MODEL_BRANDS)
        cars.create_automobile(
            brand = brand,
            model = model,
            plate = generate_plate(),
            year = random.randint(2005,2025),
            user_id = None,

            )
    total_users = len(users.query_all())
    total_addresses = len(addresses.query_all())
    total_cars = len(cars.query_all())
    session.close()

    print(f"Done!. Users: {total_users} | Address: {total_addresses} | Cars: {total_cars}")

if __name__ == "__main__":
    populate()