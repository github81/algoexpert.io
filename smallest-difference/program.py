def smallestDifference(arrayOne, arrayTwo):

	smallestDiff = []
	if len(arrayOne) == 0 or len(arrayTwo) == 0:
		return smallestDiff

    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
    
	i = 0
	j = 0
    
	diff = abs(arrayOne[i] - arrayTwo[j])
	smallestDiff = [arrayOne[i],arrayTwo[j]]
	while True:
    	 
		if arrayOne[i] == arrayTwo[j]:
			return [arrayOne[i],arrayTwo[j]]
		elif arrayOne[i] < arrayTwo[j]:
			i+=1
		else: j+=1
    	 
		if (i > len(arrayOne)-1) or (j > len(arrayTwo)-1):
			break

		if diff > abs(arrayOne[i]-arrayTwo[j]):
			diff = abs(arrayOne[i]-arrayTwo[j])
			smallestDiff = [arrayOne[i],arrayTwo[j]]

	return smallestDiff
    	 
    	 
    	 
    	 