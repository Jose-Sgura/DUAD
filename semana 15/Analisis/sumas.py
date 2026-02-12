def manual_add(n):
    result = 0#O(1)
    for i in range(1, n + 1):#O(n)
        result += i#O(1)
    return result#O(1)
#Complejidad O(n)

def add_formula(n):
    return n * (n + 1) // 2 #O(1)
#Complejidad O(1)

#Usaría "add formula" como la mejor opción debido a que el tiempo de "n" no crece
#con el tamaño del problema
