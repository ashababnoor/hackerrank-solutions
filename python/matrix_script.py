#!/bin/python3

'''
Matrix Script 
Link: https://www.hackerrank.com/challenges/matrix-script/problem
'''

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
   
full_string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
full_string = re.sub(r'(?<=[a-zA-Z0-9])[@#$%&!\s]+(?=[a-zA-Z0-9])', ' ', full_string)

print(full_string)
