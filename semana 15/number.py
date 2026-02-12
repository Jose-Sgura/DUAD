def bubble(list_sort):
    iter=0
    swaps=0

    for outer_index in range(0, len(list_sort)-1):
        change=False
        iter += 1

        for index in range(0, len(list_sort)-1-outer_index):
            if list_sort[index] > list_sort[index + 1]:
                list_sort[index],list_sort[index +1]= list_sort[index +1], list_sort[index]
                swaps += 1
                change = True
        if not change:
            break
    return list_sort, iter, swaps

def validated_bubble(data):

    if not isinstance(data, list):
        return "Error: The entrance is not a list"
    if len(data)== 0:
        return "Error: Empty List"
    
    for number in data:
        if not isinstance(number, (int,float)):
            return "Error: List has non numeric elements"
    sorted_list, iter, swaps= bubble(data.copy())

    return f"Sorted list: {sorted_list}\n iterations: {iter}\n Exchanges:{swaps}"

print(validated_bubble([5, "hola", 2]))
print(validated_bubble([]))
print(validated_bubble([5, 1, 4, 2, 3]))