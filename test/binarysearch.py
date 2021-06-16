

def binarySearch(lst,target):
	l = 0
	r = len(lst)-1
	while l <= r:
		mid = (l + r)//2
		#print("{},{},{}".format(l,r,mid))
		if lst[mid] == target:
			return mid
		elif target < lst[mid]:
			r = mid-1
		else:
			l = mid+1
	return -1
	
def binarySearchRecursion(lst,target,l,r):

	mid = (l + r)//2
	if lst[mid] == target:
		return mid
	elif target < lst[mid]:
		return binarySearchRecursion(lst,target,l,mid-1)
	elif target > lst[mid]:
		return binarySearchRecursion(lst,target,mid+1,r)
	else:
		return -1


if __name__ == '__main__':
	l = [1,2,3,4,5,6,7,8,9,10]
	print(binarySearch(l,10))
	print(binarySearch(l,1))
	print(binarySearch(l,4))
	print(binarySearchRecursion(l,10,0,9))
	print(binarySearchRecursion(l,1,0,9))
	print(binarySearchRecursion(l,4,0,9))
