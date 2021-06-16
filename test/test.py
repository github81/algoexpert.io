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
    
  
def test5():
	keyboard = "abcdef"
	key_pos = {char: i for i, char in enumerate(keyboard)}
	print(key_pos)
    
def test4():

	nums = [1,2,3,4]
	#return [res for idx in range(0,len(nums),2) for res in [nums[idx+1]]*nums[idx]] 
	
	return [x for x in range(0,100,2)]

def test6():
	
	s = 'LLRR'
	
	print(s[2:2+2])
	print(s[2]*2)

def set_list(list): 
	list = ["A", "B", "C"] 
	return list
  
def add(list): 
	list.append("D") 
	return list
  

def test7():

	testList = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
	return [y.startswith("More organized code") for y in testList]
	
def test8():

	print("test".count('a'))
	
def numberOfMatches(n):
        
	m = 0
	while n > 1:
		if n%2 == 1:
			m += n // 2 + 1
		else:
			m += n // 2			
		n = n // 2
		#print("n: " + str(n) + ", m: " + str(m))
	return m	
	

def productSumHelper(array,depth):
	
	print(array)
	print(depth)
	
	if len(array) == 0:
		return 0	
		
	if type(array[0]) is list:
		s = productSumHelper(array[0],depth+1)
	else:
		item = array[0]
		s = item * depth
		array.pop(0)
	
	return s + productSumHelper(array,depth)


def tribonacci(n):

	if n<=2:
		return (n+1)>>1
		
	a,b,c=0,1,1
	for _ in range(n-2):
		a,b,c=b,c,a+b+c
		
	return c
		

def test9():

	a,b,c = input().split()
	print(a)
	print(b)
	print(c)		



	
	

def findMissingRanges(nums,lower,upper):
        
	l = []
	isRange = False
	s = 0
	p = 0
	for i in range(lower,upper+1,1):

		if i not in nums:
			if isRange:
				p = i
				continue
			isRange = True
			s = i
		elif isRange:
			#print("{},{}".format(s,p))
			if s == p:
				l.append(str(s))
			else:
				l.append(str(s) + "-->" + str(p))
			isRange = False

		p = i

	print("{},{},{},{},{}".format(i,isRange,s,p,l))
    
	if s == p:
		l.append(str(s))
	else:
		l.append(str(s) + "-->" + str(p))            

	return l

def morse_decoder2(code):

	MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

    #replace this for solution
	ll = code.split('   ')
	cl = []
	for l in ll:
		ws = l.split(' ')
		for i in range(0,len(ws)):
			c = MORSE[ws[i]]
			if ord(c) >= 97 and ord(c) <= 122:
				c = chr(ord(c)-32)
			cl.append(c)
		cl.append(' ')         

	return "".join(cl[:len(cl)-1])

def morse_decoder(code):

	MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

	return ' '.join(''.join(MORSE[c] for c in w.split()) for w in code.split('   ')).capitalize()
	#return ' '.join(''.join(MORSE[letter] for letter in word.split()) for word in code.split('   ')).capitalize()


def encode_morse(message):
	
	char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def sum_numbers(text):
    
    return sum([x for x in text.split() if x.isdigit() == True])


def fib_fast2(num):
	
	a, b = 0, 1
	for _ in range(num-1):
		a,b=b,a+b
	
	return b


def arrayManipulation(n):

	queries = [[1,2,100],
				[2,5,100],
				[3,4,100]]
				
	queries = [
				[1,5,3],
    			[4,8,7],
    			[6,9,1]
				]
				
	queries = [ 
				[2,6,8],
				[3,5,7],
				[1,8,1],
				[5,9,15]
				]
	m = 0		
	for i in range(0,len(queries)):
		s = set(range(queries[i][0],queries[i][1]+1))
		print("s,{}".format(s))
		v = queries[i][2]
		for j in range(0,len(queries)):
			if i == j:
				continue
			s2 = set(range(queries[j][0],queries[j][1]+1))
			if len(s.intersection(s2)) > 0:
				s = s.intersection(s2)
				v += queries[j][2]
			print("{},{}".format(i,s))
		if v > m:
			m = v
	
	return m
			
		
def how_deep(structure):


	if not structure or type(structure) is int:
		return 0

	for i in structure:
		if type(i) is tuple:
			s = 1
		else:
			s = 0
			
		return s + how_deep(i)
	

def reverseCheck():

	n=1213
	num=n
	new_num=0
	
	while num:
		new_num*=10
		new_num+=num%10
		num//=10
		
	return new_num==n
	
def incomeTax():

	d = 45000
	i = 0

	d-=10000
	if d >= 10000:
		i+=10000*.10
		d-=10000
	i+=d*0.20
	
	return i	
	
def inputTest():

	num1 = int(input("Enter number 1: "))
	num2 = int(input("Enter number 2: "))
	print(num1+num2)

def tableFormat():

	starters = [
		[ 'Andre Iguodala', 4, 3, 7 ],
		[ 'Klay Thompson', 5, 0, 21 ],
		[ 'Stephen Curry', 5, 8, 36 ],
		[ 'Draymon Green', 9, 4, 11 ],	
		[ 'Andrew Bogut', 3, 0, 2 ]]
    
	row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} |".format
    
	for p in starters:
		print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))

def skipLine():

	count = 1
	with open("test1.txt", "r") as fp, open("test2.txt", "w") as wfp:
		wfp.write(fp.read())
		count+=1

def loopTest():

	for i in range(-10,0):
		print(i)
		
	for i in range(5):
		print(i)
	else:
		print("Done!")

def fibNumbers():

	n1 = 0
	n2 = 1
	
	while n2 < 100:
		n1,n2=n2,n1+n2
		
def argsTest(*args):

	for arg in args:
		print(arg,end=",")	

def sumNum(num):

	if not num:
		return 0
	else:
		return num + sumNum(num-1)		

def lowerFirst(s):

	l = []
	insertAt = 0
	for c in s:
		if c.islower():
			l.insert(insertAt,c)
			insertAt+=1
		else:
			l.append(c)
			
	return ''.join(l)
	
def reverseChunk(l):

	cs = len(l)//3
	for i in range(0,len(l),cs):
		print(l[i:i+cs],l[i:i+cs][::-1],end=" ")

def removeFromSet(s1, s2):

	s = s1.intersection(s2)
	for i in s:
		s1.remove(i)
		
	print(s1)
	
def removeFromList(l):

	s = set(l)
	t = tuple(s)
	mn = min(s)
	mx = max(s)
	
	print("unique items {}".format(list(s)))
	print("tuple {}".format(t))
	print("min {}".format(mn))
	print("max {}".format(mx))	


def createDict():

	sampleDict = { 
		"name": "Kelly",
		"age":25, 
		"salary": 8000, 
		"city": "New york" }
	
	keys = ["name", "salary"]
	
	d = {k:sampleDict[k] for k in keys}
	print(d)

def popDict():

	sampleDict = { 
		"name": "Kelly",
		"age":25, 
		"salary": 8000, 
		"city": "New york" }

	print(sampleDict)
	sampleDict['location'] = sampleDict.pop('city')
	print(sampleDict)
	
def minDict():

	sampleDict = {
		'Physics': 82,
		'Math': 65,
		'history': 60
		}
	
	print(min(sampleDict,key=sampleDict.get))

def findAlphaNumeric():

	str1 = "Emma25 is Data scientist50 and AI Expert"
	l=[]
	for w in str1.split():
	
		if any(c.isalpha() for c in w) and any(c.isdigit() for c in w):
			l.append(w)

	print(l)


def moves(arr):
    # Write your code here
    
    odd = 0
    even = len(arr)-1
    ct = 0
    while odd < even:
        if arr[odd]%2==0:
            odd+=1
        elif arr[even]%2==1:
            even-=1
        else:
            arr[odd],arr[even]=arr[even],arr[odd]
            ct+=1
            odd+=1
            even-=1

    return ct
    
#def countCounterfeit(serialNumber):
	# Write your code here

#    w = 0

#	for sNo in serialNumber:
#		# there are 10 to 12 characters
#		if len(sNo)<10 or len(sNo)>12:
#			continue
    
		# the first 3 characters are distinct
#		if len(set(sNo[0:3])) != 3:
#			continue

		# the first 3 chacters are uppercase
#    	if sum([1 for c in sNo[0:3] if not c.isupper()]) > 0:
#			continue
    
	    #the next four characters represent the year between 1900 and 2019 inclusive
#    	import re
#	    if len(re.findall("^(19[0-9][0-9]|20[0-1][0-9])$",sNo[3:7])) == 0:
#			continue
			
	    #the next characters reprent currency denomiation 10,20,50,100,200,500,1000
    	#and the last character represent a single upper chase character
#	    if len(re.findall("^([125]{1}[0]{1}[0]{0,1}[0]{0,1}[A-Z]{1})$",sNo[7:])) == 0:
#			continue
			
		#sum the valid currency values
#		w+=int(sNo[7:][:-1])

#    return w
    
def regex_test():

	# Regex Lookbehind example
	example = re.search(r'(?<=geeks)\w', 
                    'geeksforgeeks')
  
	print(example.group())
	print("Pattern found from index", example.start(), example.end())
	
def tallest_tower():

	lst = [[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 1, 0, 1, 0],
		[0, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1]]
	
	for i in zip(*lst):
		print(i)
	
	

def countPrimes(n):
        
	if n <= 2:
		return 0

	c = 0
	for i in range(2,n+1):
		for j in range(1,i):
			if i%j == 0:
				print(i) 

if __name__ == '__main__':

	countPrimes(10)

	#tallest_tower()

	#print(regex_test())

	#findAlphaNumeric()

	#minDict()

	#popDict()

	#print(createDict())

	#removeFromList([87, 45, 41, 65, 94, 41, 99, 94])

	#firstSet  = {23, 42, 65, 57, 78, 83, 29}
	#secondSet = {57, 83, 29, 67, 73, 43, 48}
	
	#removeFromSet(firstSet, secondSet)

	#sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
	#reverseChunk(sampleList)

	#print(lowerFirst("PyNaTive"))

	#print(sumNum(10))

	#argsTest('this','is','just','the','begining')

	#fibNumbers()

	#print(loopTest())

	#print(skipLine())

	#tableFormat()	

	#inputTest()

	#print(incomeTax())
	
	#pynative()
	#print(reverseCheck())

	#t = ((1, 2, (3,)))
	#t = (1, 2, (3, (4,)))
	#print(how_deep(t))

	#print(arrayManipulation(10))

	#print(fib_fast2(10))

	#print(sum_numbers("1 2 3"))

	#print(morse_decoder('... --- ...'))
	#print(morse_decoder('... --- -- .   - . -..- -'))

	#nums = [0,1,3,50,75]
	#lower = 0
	#upper = 99
	#print(findMissingRanges(nums,lower,upper))

	#test9()

	#print(tribonacci(0))
	#print(tribonacci(1))
	#print(tribonacci(10))

	#array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
	#print(productSumHelper(array,1))

	#print(numberOfMatches(14))
	#print(numberOfMatches(7))

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
	#test3()
	#print(test4())
	#test5()
	#test6()

	#my_list = ["E"] 
	#print(set_list(my_list)) 
	#print(add(my_list)) 
	
	#print(test7())
	#test8()







	

		