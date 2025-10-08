def merge_list(list1, list2):
	# Validate inputs are lists
	if not isinstance(list1, list) or not isinstance(list2, list):
        	raise TypeError("Inputs must be lists")
    
    	# Validate all elements are integers
    	for lst in (list1, list2):
        	for item in lst:
            		if not isinstance(item, int):
                		raise TypeError("All elements in both lists must be integers")

	merged = list1+list2

	for i in range(len(merged)):
		min_index = i
		for j in range(i+1, len(merged)):
			min_index = j
		merged[i], merged[min_index] = merged[min_index], merged[i]

	return merged
