def merge_list(list1, list2):
    
	mergedList = []
	for item in list1:
		if not isinstance(item, int):
			raise TypeError("Varaible type must be integer")
		mergedList.append(item)
		
	for item in list2:
		if not isinstance(item, int):
			raise TypeError("Variable type must be integer")
		mergedList.append(item)
		
	n = len(mergedList)

	for i in range(n-1):
		for j in range(0, n-i-1):
			if mergedList[j] > mergedList[j+1]:
				mergedList[j], mergedList[j+1] = mergedList[j+1], mergedList[j]