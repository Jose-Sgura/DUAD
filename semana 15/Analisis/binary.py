def linear_search(my_list, target):
    for item in my_list:#O(n)
        if item == target:#O(1)
            return True #O(1)
    return False #O(1)
#complejidad: O(n)


def binary_search(my_list, target):
    low = 0 #O(1)
    high = len(list) - 1 #O(1)
    while low <= high: #O(log n) se ejecuta log n veces
        mid = (low + high) // 2 #O(1)
        if my_list[mid] == target:#O(1)
            return True #O(1)
        elif my_list[mid] < target:#O(1)
            low = mid + 1 #O(1)
        else: #O(1)
            high = mid - 1 #O(1)
    return False #O(1)
    
    #complejidad O(log on)

#linear_search es conveniente usarla 
#cuando la lista no está ordenada o es pequeña

#binary_search se utiliza cuando la lista
#ya está ordenada 

#¿Qué pasa si la lista no está ordenada?
#para linear_search no habría problema ya que 
#recorrería la lista hasta dar con el target
#sin embargo es mas lento el proceso si la lista es grande

#mientras que binary_search no daría
#con el target ya que primero inicia con el medio
#si la mitad es menor al target entonces buscaría
#hacía la derecha si la nuevo mitad es mayor buscaría
#a la izquierda, quedandose sin elementos para buscar
#por lo que binary precisa de una lista ordenada