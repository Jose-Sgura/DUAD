#1.Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def first_function():
    incredible=2+2
    print(f'Programing rules {incredible}!')
    second_function()

def second_function():
    print('This is amazing')

first_function()

#2.Experimente con el concepto de scope:
    #1. Intente accesar a una variable definida dentro de una función desde afuera.
    #2.  Intente accesar a una variable global desde una función y cambiar su valor.
#1.
def experiment():
    numering=1+2+3
    return numering

total=experiment()
print(f'The sum total is {total}')

#2
golbal='moms'

def women():
    global Golbal
    Golbal= 'Fahter and Mother'

women()
print(f'She is {Golbal} at the same time')

#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    #2. [4, 6, 2, 29] → 41

def sum(pist):
    plus=0
    for counter in pist:
        plus+=counter
    return plus
total=sum([4,6,2,29])
print(f'The sum result is {total}')

#4 Cree una función que le de la vuelta a un string y lo retorne.
    #1. Esto ya lo hicimos en iterables.
    #2. “Hola mundo” → “odnum aloH”

def backingoff(string):
    return string[::-1]
    
structure=backingoff('Hola Mundo')
print('The word backwards is-----'  + structure)

#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    #1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
def indentifier(text):
    capital=0
    lower=0
    for char in text:
        if char.isupper():
            capital+=1
        elif char.islower():
            lower+=1
    print(f'for the word ---I love Nación Sushi--- are {capital} upper cases and {lower} lower cases')

indentifier('I love Nación Sushi')
    

#6 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    #1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    #2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def wordorder(string):
    wordList= string.split('-')
    orderedList= sorted(wordList)
    endup='-'.join(orderedList)
    return endup

endup=wordorder('python-variable-funcion-computadora-monitor')
print(endup)

#7.7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    #1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    #2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    #3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def qualifyingprime(number):
    if number<2:
        return False
    for index in range(2,int(number**0.5)+1):
        if number%index==0:
            return False
    return True
def numberlist(enlist):
    prime=[]
    for n in enlist:
        if qualifyingprime(n):
            prime.append(n)
    return prime

result=numberlist([1,4,6,7,13,9,67])
print(result)