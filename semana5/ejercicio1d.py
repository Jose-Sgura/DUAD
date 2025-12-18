#ejericico1
#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay','en', 'que','interacción', 'indices','muy']

second_list = ['casos', 'los', 'la', 'por', 'es','util']

for index in range(len(first_list)):
    print(f'{first_list[index]} {second_list[index]}')












#ejercicios de diccionarios faltantes
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


#2 Cree un programa que cree 
# un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.


    province= ['Alajuela','Heredia', 'Puntarenas','Guanacaste']
    Cantones= ['San Carlos','San Rafael','Osa','Nicoya']
    

Lists = dict(zip(province,Cantones))
print(Lists)



#3 Cree un programa que use una lista para eliminar keys de un diccionario.
Empleoyee= {
    'Name':'Jose',
    'Email':'josee9425@gmail.com',
    'AccesLevel': 7,
    'Age':29
}
Rid_the_shit_out=['AccesLevel','Age']

for remove in Rid_the_shit_out:
    Empleoyee.pop(remove,None)

print(Empleoyee)

#4 Dada una lista de ventas con la siguiente información:
#date
#customer_email
#items
#Y cada item teniendo la siguiente información:
#name
#upc
#unit_price
#Cree un diccionario que guarde el total de ventas de cada UPC.
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

Total={}
for sell in sales:
    for item in sell['items']:
        upc=item['upc']
        cost=item['unit_price']
        Total[upc]=Total.get(upc,0)+cost

for UP,result in Total.items():
    print(f'UPC:{UP},Total en ventas:${result}')