def insertionSort(array):
    # Write your code here.
	for i in range(0,len(array)-1):
		for j in range(i+1,0,-1):
			print(str(j) + "," + str(j-1))
			if array[j-1] > array[j]:
				array[j], array[j-1] = array[j-1], array[j]
			else:
				break
	return array
