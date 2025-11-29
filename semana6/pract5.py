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