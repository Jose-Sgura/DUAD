#1. Cree un algoritmo que le pida 2 números al usuario, 
# los guarde en dos variables distintas (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.

print('Please enter 2 numbers')
print('They will be ordered from lowest to highest')
first=int(input('enter the second number'))
second=int(input('enter the second number'))

if first > second:
    temp=first
    first=second
    second=temp
print(f'The order from lowest to highes is : {first} y {second}')