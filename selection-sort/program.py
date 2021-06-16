def minimumIndex(beginIndex, array):
	minIndex = beginIndex
	for i in range(beginIndex,len(array)):
		if array[i] < array[minIndex]:
			minIndex = i
	return minIndex

def selectionSort(array):
    # Write your code here.
	for idx in range(0,len(array)):
		minIndex = minimumIndex(idx,array)
		print(minIndex)
		if minIndex != idx:
			minNum=array[minIndex]
			array.pop(minIndex)
			array.insert(idx,minNum)
		
	return array
