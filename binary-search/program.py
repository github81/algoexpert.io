
def binarySearchHelper(leftIndex, arrayLength, array, target):
	if leftIndex > arrayLength:
		return -1
	index = (leftIndex + arrayLength)//2
	print(str(index) + "," + str(leftIndex) + "," + str(arrayLength) + "," + str(target))
	if target == array[index]:
		return index
	elif target < array[index]:
		return binarySearchHelper(leftIndex,index-1,array,target)
	else:
		return binarySearchHelper(index+1,arrayLength,array,target)


def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(0,len(array)-1,array,target)
    
    	
