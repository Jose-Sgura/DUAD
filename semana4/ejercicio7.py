#Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor

print('type 5 numbers')
one = int(input('first number'))
two = int(input('Second number'))
three = int(input('third number'))
four = int(input('fourth number'))
fift = int(input('Fift number'))

Largest= max (one,two,three,four, fift)
print(f'The largest would be {Largest}')