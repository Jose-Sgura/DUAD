import random
from faker import Faker
from db import PgManager

fake = Faker()

NUM_USERS = 200
NUM_AUTOMOBILES = 100
MIN_RENTALS = 50
MAX_RENTALS = 150

USER_STATUSES = ["Active", "Inactive"]
AUTO_STATUSES = ["Available", "Rented", "Maintenance", "Reserved"]
RENTAL_STATUSES = ["Active", "Completed", "Cancelled"]

BRANDS_MODELS = {
    "Toyota": ["Corolla", "Camry", "Rav4", "Hilux", "Yaris"],
    "Honda": ["Civic", "Accord", "CRV", "Fit", "HRV"],
    "Ford": ["Focus", "Fiesta", "Explorer", "Ranger", "Escape"],
    "Kia": ["Rio", "Sportage", "Picanto", "Seltos", "Soul"],
    "Hyundai": ["Accent", "Tucson", "Elantra", "Creta", "i10"],
}

def seed_users(db_manager, count):
    user_ids = []
    for i in range(count):
        full_name = fake.name()[:30]
        email = f"user{i}@mail.com"
        user_name = fake.user_name()[:20]
        password = fake.password(length = 10)
        birth_date = fake.date_of_birth(minimum_age = 18, maximum_age = 70)
        status = random.choice(USER_STATUSES)

        result = db_manager.execute_query(
            "INSERT INTO lyfter_car_rental.users "
            "(full_name, email, user_name, password, birth_date, status) "
            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;",

            full_name, email, user_name, password, birth_date, status
            )
        user_ids.append(result[0][0])
    print(f"{len(user_ids)} created users")
    return user_ids

def seed_automobiles(db_manager, count):
    auto_ids = []

    for _ in range(count):
        brand = random.choice(list(BRANDS_MODELS.keys()))
        model = random.choice(BRANDS_MODELS[brand])
        manufacturing_year = random.randint(2005, 2024)
        status = random.choice(AUTO_STATUSES)

        result = db_manager.execute_query(

            "INSERT INTO lyfter_car_rental.automobile "
            "(brand, model, manufacturing_year, status) "
            "VALUES (%s, %s, %s, %s) RETURNING id;",
            brand, model, manufacturing_year,status
        )
        auto_ids.append(result[0][0])
    print(f"{len(auto_ids)} created automobiles")
    return auto_ids

def seed_rentals(db_manager, user_ids, auto_ids):
    num_rentals = random.randint(MIN_RENTALS, MAX_RENTALS)
    created = 0
    for _ in range(num_rentals):
        user_id = random.choice(user_ids)
        auto_id = random.choice(auto_ids)
        status = random.choice(RENTAL_STATUSES)

        db_manager.execute_query(
            "INSERT INTO lyfter_car_rental.rent (user_id, auto_id, status) "
            "VALUES (%s, %s, %s);",
            user_id, auto_id, status,
            )
        created+=1
    print(f"{created} created rents")

def run_seed():
    db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="tu_nueva_contraseña",
        host="localhost",
)

    user_ids = seed_users(db_manager, NUM_USERS)
    auto_ids = seed_automobiles(db_manager, NUM_AUTOMOBILES)
    seed_rentals(db_manager, user_ids, auto_ids)

    db_manager.close_connection()

if __name__ == "__main__":
    run_seed()

