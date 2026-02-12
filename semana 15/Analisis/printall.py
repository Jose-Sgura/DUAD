def print_all_pairs(my_dict):
    for key1 in my_dict: #O(n)
        for key2 in my_dict: #O(n²)
            print(f"{key1}-{key2}") #O(1)
        #complejidad O(n²)

#asumiento que el print tarde un aproximado de 1 microsegundo 1 millon con
#complejidad temporal de n² aumentaría a 1,000,000,000,000 (1,000,000 x 1,000,000),
#entonces 1,000,000,000,000 x 0.000001 s = 1,000,000 segundos


