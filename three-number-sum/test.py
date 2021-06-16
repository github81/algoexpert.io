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
		print("valid")
	else:
		print("invalid")
    
if __name__ == '__main__':
	n = int(input())
	cardNumberList=[]
	for i in range(n):
		cardNumber = input()
		cardNumberList.append(cardNumber)
		
	for idx,cardNumber in enumerate(cardNumberList):
		validateCreditCard(str(cardNumber))
	#validateCreditCard("4567-3423-2343-2333")
	#validateCreditCard("4567-4567-4567-7778")
