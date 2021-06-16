def isMonotonic(array):
    # Write your code here.
	if len(array) == 1:
		return True
	
	direction=0
	for idx in range(1,len(array)):
		
		if direction == 1 and array[idx] < array[idx-1]:
			print("returning 1")
			return False

		if direction == 2 and array[idx] > array[idx-1]:
			print("returning 2")
			return False

		if array[idx] == array[idx-1]:
			continue
		elif array[idx] > array[idx-1]:
			direction = 1
		else:
			direction = 2
			
		#print(str(idx) + "," + str(array[idx]) + "," + str(idx-1) + "," + str(array[idx-1]) + "," + str(direction))

	return True

    	 
    	 