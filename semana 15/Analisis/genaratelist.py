def generate_list_trios(list_a, list_b, list_c):
	result_list = []#O(1)
	for element_a in list_a:#0(n)
		for element_b in list_b:#0(n²)
			for element_c in list_c:#O(n³)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(1)
				
	return result_list#O(1)