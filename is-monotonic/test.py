import re

def printNumberAsString():
	sum = 0
	tempSum = 0
	multiplier = 10
	for idx in range(1,n+1):
		if idx >= 10:
			multiplier = 100
		if idx >= 100:
			multiplier = 1000
		
		sum = sum * multiplier + idx
		#print(str(multiplier) + "\t" + str(idx) + "\t" + str(tempSum) + "\t" + str(sum))

def validateCreditCard(cardNumber):
	#match=re.search(r"^(4|5|6)[\d]{3}-?[\d][4]-?[\d]{4}-?[\d]{4}$",str(cardNumber))
	matchNumbers=re.search(r"^(4|5|6)[\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$",str(cardNumber))

	newCardNumber=re.sub(r'-', '', cardNumber)	
	matchNonRepeats=re.search(r'(\d)\1{3}',newCardNumber)
	if matchNumbers is not None and matchNonRepeats is None:
		print("Valid")
	else:
		print("Invalid")


		
def test():
	alternate=True
	s="0100"
	zeroWays = 0
	oneWays = 0
	for idx in range(len(s)):
	
		if alternate:
			alternate = False
			if s[idx] == '1':
				zeroWays+=1
			else:
				oneWays+=1
		else:
			alternate = True   
			if s[idx] == '1':
				oneWays += 1
			else:
				zeroWays += 1
				
	return zeroWays if zeroWays < oneWays else oneWays
	
	
def test2():
	s = "leetcodeisacommunityforcoders"
	vowels = ['a','e','i','o','u']

	newString = []
	for idx, item in enumerate(s):
		if item not in vowels:
			newString.append(item)
	
	return "".join(newString)
    
def shuffle2():

	nums = [2,5,1,3,4,7]
	n = 3
	newList = []
	for i in range(n):
            
		newList.append(nums[i])
		newList.append(nums[i+n])
  
	return newList 
    
def test3():

	print(234%10)
	print(23%10)
	print(2%10)
    
if __name__ == '__main__':
	#n = int(input())
	#cardNumberList=[]
	#for i in range(n):
	#	cardNumber = input()
	#	cardNumberList.append(cardNumber)
		
	#for idx,cardNumber in enumerate(cardNumberList):
	#	validateCreditCard(str(cardNumber))
	#validateCreditCard("4567-3423-2343-2333")
	#validateCreditCard("4567-4567-4567-7778")

	#print(test())
	#print(test2())
	test3()


	
	






	

		