from db import test_connection, verify_create_tables, get_session
from manager import UserManager, AutomobileManager, AddressManager

def line(title:str)-> None:
    print("\n" + "-" *60)
    print(title)
    print("-"*60)

def main()->None:
    # Probar la conexion antes de intentar cualquier otra cosa
    if not test_connection():
        return
    # Validar/crear tablas (Ejercicio 3)
    verify_create_tables()
    session = get_session()
    users= UserManager(session)
    cars = AutomobileManager(session)
    addresses = AddressManager(session)

    #Crear usuarios
    line("Creating users")
    ana = users.create_user("Ana Lopez", "ana@example.com","6440-5390")
    benjamin = users.create_user("Benjamin Smith", "benjamin@example.com","8661-1733")
    print(ana)
    print(benjamin)
    
    #Crear direcciones (siempre con usuario_id obligatorio)
    line("Creating addresses")
    add_ana = addresses.create_address("5a Avenue 10-20", "Guatemala City","01001", ana.id)
    add_benjamin = addresses.create_address("Real Street 3-45", "SanCarlos","01002", benjamin.id)
    print(add_ana)
    print(add_benjamin)

    fail_address = addresses.create_address("Fake Street 1-2", "Nowhere","00000", user_id = 9999)
    print("Address with unexisting user_id ->", fail_address)

    #Crear automoviles: uno con dueño, otro SIN dueño
    line("Creating automobiles")
    car_ana = cars.create_automobile("Toyota", "Corolla", "P123ABC", 2020, user_id = ana.id)
    car_no_owner = cars.create_automobile("Honda", "Civic", "P456DEF", 2021)
    print(car_ana)
    print(car_no_owner)

    #Asociar el automovil huerfano a un usuario
    line("Afiliating car with no owner to Benjamin")
    car_no_owner = cars.affiliate_user(car_no_owner.id, benjamin.id)
    print(car_no_owner)
    
    #modificar datos existentes
    line("Modifying data")
    ana = users.modify_user(ana.id, phone = "5555-20200")
    print("Modified user:", ana)
    car_ana = cars.modify_automobile(car_ana.id, year = 2021)
    print("Modified car:", car_ana)
    dir_benjamin = addresses.modify_address(add_benjamin.id, city = "San Marcos")
    print("Modified address:", dir_benjamin)

    # Consultar todos los registros de cada tabla
    line("Querying all users")
    for u in users.query_all():
        print(u)

    line("Querying all automobiles")
    for c in cars.query_all():
        print(c)

    line("Querying all addresses")
    for a in addresses.query_all():
        print(a)

    # Eliminar un automovil
    line("Deleting car of Benjamin")
    deleted = cars.delete_automobile(car_no_owner.id)
    print("Deleted? ", deleted)

    line("Querying the rest of automobiles")
    for r in cars.query_all():
        print(r)
    
    session.close()
if __name__ == "__main__":
    main()