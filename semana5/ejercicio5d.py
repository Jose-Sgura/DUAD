#ejercicio5
#Cree un programa 
# que le pida al usuario 10 números, y al final le muestre 
#todos los números que ingresó, seguido del numero ingresado más alto

numbers= []

for index in range(10):
    number = float(input(f'Ingrese el número {index+1}:'))
    numbers.append(number)

print(f'Los números ingresados son {numbers}')
    

Longest_Number= max(numbers)
print(f'El número mayor es: {Longest_Number}')