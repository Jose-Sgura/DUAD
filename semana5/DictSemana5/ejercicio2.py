#2 Cree un programa que cree 
# un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.


province= ['Alajuela','Heredia', 'Puntarenas','Guanacaste']
Cantones= ['San Carlos','San Rafael','Osa','Nicoya']
    

Lists = dict(zip(province,Cantones))
print(Lists)