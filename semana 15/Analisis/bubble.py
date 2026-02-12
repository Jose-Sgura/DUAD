def bubble_right_to_left(list_to_sort):
    
    for outer_index in range(0, len(list_to_sort)-1):#O(n)

        has_made_change=False#O(1)

        for i in range(len(list_to_sort)-1, outer_index,-1):#O(n)
        
            current_element = list_to_sort[i]#O(1)
            previous_element = list_to_sort[i - 1]#O(1)
    
            print(f"--Iter: {outer_index},{i}." f"Current Element: {current_element},"f"Previous Element: {previous_element}")#O(1)

            if current_element < previous_element:#O(1)
                print("The element is minor than the previous one, exchange them")#O(1)

                list_to_sort[i] = previous_element#O(1)
                list_to_sort[i - 1] = current_element#O(1)
                has_made_change = True#O(1)
        if not has_made_change:#O(1)
            break #O(1)

my_test_list = [9, 8, 7, 6, 5, 4, 3, 1,2]#O(1)
bubble_right_to_left(my_test_list)#O(n²)
print(my_test_list)#O(1)