from typing import List

def even_odd(A: List[int]) -> None:
	next_even, next_odd = 0, len(A)-1
	while next_even < next_odd:
		if A[next_even]%2 == 0:
			next_even += 1
		else:
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1

if __name__=='__main__':
	A = [5,6,2,46,732,6,5,12323,657234,4526]
	print(A)
	even_odd(A)
	print(A)