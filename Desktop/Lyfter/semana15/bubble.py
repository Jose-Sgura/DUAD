def bubble_right_to_left(list_to_sort):
    
    for outer_index in range(0, len(list_to_sort)-1):

        has_made_change=False

        for i in range(len(list_to_sort)-1, outer_index,-1):
        
            current_element = list_to_sort[i]
            previous_element = list_to_sort[i - 1]
    
            print(f"--Iter: {outer_index},{i}." f"Current Element: {current_element},"f"Previous Element: {previous_element}")

            if current_element < previous_element:
                print("The element is minor than the previous one, exchange them")

                list_to_sort[i] = previous_element
                list_to_sort[i - 1] = current_element
                has_made_change = True
        if not has_made_change:
            break

my_test_list = [9, 8, 7, 6, 5, 4, 3, 1,2]
bubble_right_to_left(my_test_list)
print(my_test_list)