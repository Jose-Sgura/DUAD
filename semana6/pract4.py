#4 Cree una función que le de la vuelta a un string y lo retorne.
    #1. Esto ya lo hicimos en iterables.
    #2. “Hola mundo” → “odnum aloH”

def backingoff(string):
    return string[::-1]
    
structure=backingoff('Hola Mundo')
print('The word backwards is-----'  + structure)
