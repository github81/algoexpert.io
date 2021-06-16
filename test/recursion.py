

def bunnyEars(bunnies):

	if not bunnies:
		return 0
	else:
		return 2 + bunnyEars(bunnies-1)


def bunnyEars2(bunnies):

	if not bunnies:
		return 0
	
	extraEar = 0
	if bunnies%2==1:
		extraEar = 1
	
	return 2 + extraEar + bunnyEars2(bunnies-1)

def triangle(rows):

	if not rows:
		return 0
	elif rows == 1:
		return 1
	else:
		return 2 + triangle(rows-1)
		

def sumOfDigits(n):

	if not n:
		return 0
	elif n < 10:
		return n
	elif n == 10:
		return 1
	else:
		return n%10 + sumOfDigits(n//10)
		
def count7(n):

	print(n)

	if not n:
		return 0
	else:
		val = 0
		if n%10 == 7:
			val = 1
		return val + count7(n//10)
		

def count(n):

	if n == 0:
		return 0
	elif n < 10:
		return 1
	else:
		return 1 + count(n//10)
    
    
def fib_fast(num):

	if num == 0:
		return 0
	
	if num == 1:
		return 1
		
	return fib_fast(num-1) + fib_fast(num-2)

def how_deep2(structure,n=1):

	return max([n] + [how_deep2(e,n+1) for e in structure if type(e) is tuple])


def how_deep(structure, n=1):
    return max([n] + [how_deep(s, n+1) for s in structure if isinstance(s, tuple)])


def flat_list2(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flat_list(S[0]) + flat_list(S[1:])
    return S[:1] + flat_list(S[1:])

def flat_list(S):

	if type(S) is list:
		if len(S) == 0:
			return []
		first, rest = S[0] , S[1:]
		return flat_list(first) + flat_list(rest)
	else:
		return [S]

def sum_recursive(current_number, accumulated_sum):
	# Base case
	# Return the final state
	if current_number == 11:
		print(accumulated_sum)
		return accumulated_sum

	# Recursive case
	# Thread the state through the recursive call
	else:
		return sum_recursive(current_number + 1, accumulated_sum + current_number)


def attach_head(element, input_list):
	return [element] + input_list

from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci_recursive(n):
	
	if n == 0:
		return 0
		
	elif n == 1:
		return 1
		
	else:
		return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
		

def flatDict(pyobj, keystring=''):
    if type(pyobj) == dict:
        keystring = keystring + '/' if keystring else keystring
        for k in pyobj:
            yield from flatDict(pyobj[k], keystring + str(k))
    else:
        yield keystring, pyobj


if __name__ == '__main__':

	d = {
		"name": {
		"first": "One",
		"last": "Drone"
		},
		"job": "scout",
		"recent": {},
		"additional": {
			"place": {
				"zone": "1",
				"cell": "2"}
				}
			}

	for k, v in flatDict(d):
		print("{},{}".format(k,v))
	

	#print(fibonacci_recursive(1500))
	
	#print(attach_head(10,attach_head("hello",[])))
	
	#print(sum_recursive(0,1))
	#print(flat_list([1, 2, 3]))
	#print(flat_list([1, [2, 2, 2], 4]))
	#print(how_deep3((1, 2, (3, (4,)))))
	
	#print(fib_fast(10))
	#print(count(111111))
	
	#print(bunnyEars(10))
	#print(bunnyEars2(10))
	#print(triangle(5))
	#print(sumOfDigits(10002))
	#print(count7(7777001))