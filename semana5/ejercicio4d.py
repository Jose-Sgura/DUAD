#ejercicio4
#Cree un programa que elimine todos los números impares de una lista.

Deleted_Odd  = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for index in range(len(Deleted_Odd)-1,-1,-1):
        if Deleted_Odd[index]% 2!=0:
            Deleted_Odd.pop(index)

print(f'With no odds!{Deleted_Odd}')