Lastname= 'Segura Cubero'

Name = 'Jose Manuel' + Lastname

print(Name)


Sume = 10+5
String = f'La suma es = {Sume}'
print(String)

Age = 49
Employed = f'{Age} es la edad de Ramon'
print(Employed)

Animals = ['neko','inu', 'Cat', 'Dog']


print('Neko is =' + Animals[2] + '--in japonais')
print('Inu is = ' + Animals[3]+ '--in japonais')
print('Dog is ='+ Animals[1]+ '--in Spanish')
print('Cat is ='+ Animals[0]+ '--in Spanish')

Reproduction = ['Baby', 'No baby','WTF!']
People = ['Man', 'Woman']
print(People[0],'+', People[1],'=',Reproduction[0])
print(People[1],'+',People[1], '=',Reproduction[1] )
print(People[0],'+',People[0], '=',Reproduction[2] )


Flt = 1.5
Int = 50
result = 50 * 1.5

print(result)

Android = False
Human = True

if Human:
    print('It is a human let him alive') 
elif Android:
    print('it is a Android! shut it off!')

#ejericio2 

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

#ejercicio3
import random
secret = random.randint(1,10)

print('Guess a number from 1 to 10')


while True:
    Try = int(input("Type your number down :  "))

    if Try < secret:
        print("Too low, try again")
    elif Try > secret:
        print("Too high, try again")
    else:
        print(f"!Congrats!, you guessed the number, It was {secret}")
        break


#ejercicio4

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

#ejericio 5

NotesCounter = 1
NonaprovedAmount = 0
AprovedAmount = 0
AprovedAvarage = 0
NonaprovedAvarage = 0
TotalAvarage=0
TotalScore=int(input('Ingrese la cantidad de notas'))

while NotesCounter: TotalScore
CurrentScore = int(input('Add the score: '))
    
if CurrentScore < 70:
    NonaprovedAmount += 1
    NonaprovedAvarage += CurrentScore
else:
    AprovedAmount += 1
    AprovedAvarage += CurrentScore

    TotalAvarage += CurrentScore / TotalScore
    NotesCounter += 1
    if AprovedAmount > 0:
        AprovedAvarage  = AprovedAvarage  / AprovedAmount
    else:
        AprovedAvarage = 0

    if NonaprovedAmount > 0:
        NonaprovedAvarage = NonaprovedAvarage / NonaprovedAmount
    else:
        NonaprovedAvarage = 0

TotalAvarage = TotalAvarage 

print('The student has this amount of notes')
print(f'{AprovedAmount}')
print('This is the avarage of the aprovedscore')
print(f'{AprovedAvarage}')
print('The student has this amount of nonaproved score')
print(f'{NonaprovedAmount}')
print('This is the average of the nonaproved score')
print(f'{NonaprovedAvarage}')
print('This is the total score')
print(f'{TotalAvarage}')
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
#Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor

print('type 5 numbers')
one = int(input('first number'))
two = int(input('Second number'))
three = int(input('third number'))
four = int(input('fourth number'))
fift = int(input('Fift number'))

Largest= max (one,two,three,four, fift)
print(f'The largest would be {Largest}')