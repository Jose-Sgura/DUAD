print('Type 3 numbers')
one = int(input('First number'))
two = int(input('Second number'))
three = int(input('third number'))

if one>two and one>three:
    print(f'The largest number is {one}')
elif two > one and two> three:
    print((f'The largest number is {two}'))
elif three > one and three> two:
    print((f'The largest number is {three}'))