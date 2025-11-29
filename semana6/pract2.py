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