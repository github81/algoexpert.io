def runLengthEncoding(string):
    # Write your code here.
	print(string)
	prevChar = string[0]
	itemCount = 0
	runLengthChars = []
	for i,item in enumerate(string):
		print(str(item) + "," + str(prevChar) + "," + str(itemCount))
		if item != prevChar or itemCount == 9:
			runLengthChars.append(str(itemCount))
			runLengthChars.append(prevChar)
			itemCount = 1
		else:
			itemCount += 1
		prevChar = item
		if (i == len(string)-1):
			runLengthChars.append(str(itemCount))
			runLengthChars.append(prevChar)
		
	print(runLengthChars)
	return "".join(runLengthChars)