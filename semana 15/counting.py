def bubble_sort(list_sort):
    iter=0
    switches=0

    for outer_index in range(0,len(list_sort)-1):
        
        change=False
        iter += 1

        for i in range(0,len(list_sort)-1 - outer_index):
            current_element=list_sort[i]

            next_element=list_sort [i + 1]

            if current_element > next_element:

                list_sort[i] = next_element
                list_sort[i+1] = current_element
                
                switches += 1
                change=True

        if not change:
            break

    return list_sort, iter, switches

list = [5,1,4,2,3]

sorted_list, iter, switches=bubble_sort(list)

print("Set Up:", sorted_list)
print("Iteration:", iter)
print("Swaps", switches)
