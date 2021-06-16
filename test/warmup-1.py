
def sleepIn(weekday, vacation):

	return True if not weekday or vacation else False
	
def monkeyTrouble(aSmile, bSmile):

	return True if (aSmile and bSmile) or (not aSmile and not bSmile) else False

if __name__ == '__main__':

	#print(sleepIn(False,False))
	#print(sleepIn(True,False))
	#print(sleepIn(False,True))
	
	print(monkeyTrouble(True,True))
	print(monkeyTrouble(False,False))
	print(monkeyTrouble(True,False))