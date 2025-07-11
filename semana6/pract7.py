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