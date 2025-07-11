#1.Cree un diccionario que guarde la siguiente información sobre un hotel:

Management=  {
    "Name": "Marriot", 
    "Stars_Number":"7 estrellas", 
    "Rooms":[
        {
        "number":1,
        "Floor":1,
        "Price per night": 25000
        },
        { "number":20,
        "Floor":2,
        "Price per night": 45000
        },{"number":45,
        "Floor":3,
        "Price per night": 50000}
    ]}

print(Management["Name"])
print(Management["Stars_Number"])
for Huts in Management["Rooms"]:
    print(f"Room {Huts['number']} - Floor:{Huts['Floor']} - Price per night:¢{Huts['Price per night']}")