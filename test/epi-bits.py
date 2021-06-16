
def count_bits(x: int) -> int:
	num_bits = 0
	while x:
		print("{},{}".format(x,x & 1))
		num_bits += x & 1
		x >>= 1
		
	return num_bits

def parity(x: int) -> int:
	result = 0
	while x:
		result ^= x & 1
		x >>= 1
	return result

def parity2(x: int)	-> int:
	result = 0
	while x:	
		print("{},{}".format(x,x-1))
		result ^= 1
		x &= x - 1
	return result	

if __name__ == '__main__':

	#print(count_bits(12))
	#print(parity(13))
	print(parity2(13))
