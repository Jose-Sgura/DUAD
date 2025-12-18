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
