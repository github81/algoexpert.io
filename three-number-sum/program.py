def threeNumberSum(array, targetSum):
	# Write your code here.

	array.sort()

	threeSumList = []
	for idx, item in enumerate(array):
		rp = len(array)-1
		lp = idx + 1
		while lp < rp:
			leftItem = array[lp]
			rightItem = array[rp]
			tempSum = item + leftItem + rightItem
			if tempSum == targetSum:
				threeSumList.append([item,leftItem,rightItem])
				#print(str(item) + "," + str(leftItem) + "," + str(rightItem))
				lp+=1
				rp-=1
			elif tempSum < targetSum:
				lp+=1
			else: rp-=1
				
	return threeSumList	
