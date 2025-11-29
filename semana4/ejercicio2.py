name = input('Type your name')
lastname = input('Type your lastname')
Age= int(input('Type your age'))
print('Yor full name is: '+ name, lastname)
print (f'You are {Age} years old')

if Age < 3:
    print('It is a baby')
elif Age <10:
    print('It is a kid')
elif Age <15:
    print('It is a pre-teen')
elif Age <18:
    print('It is a teenager')
elif Age <25:
    print('It is a young adult')
elif Age <65:
    print('It is an adult')
elif Age <= 100:
    print('It is a elderly person')
