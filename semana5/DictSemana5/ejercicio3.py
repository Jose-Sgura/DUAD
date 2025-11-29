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