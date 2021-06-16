import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

l = [None] * (n*m)
i = 0

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
    for j in range(len(matrix_item)):
        l[i+(j*n)] = matrix_item[j]
    i+=1
    
print(l)