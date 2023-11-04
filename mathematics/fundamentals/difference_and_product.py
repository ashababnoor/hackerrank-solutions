'''
Difference and Product
Link: https://www.hackerrank.com/challenges/difference-and-product/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER p
#

def solve(d, p):
    if d < 0:
        # absolute difference is never negative
        return 0
    if d == 0 and p == 0:
        # only possible when (a, b) = (0, 0)
        return 1
    if d == 0 and p != int(p**0.5)**2:
        # if absolute difference is zero then product must be a square number 
        return 0
    if d == 0 and p == int(p**0.5)**2:
        return 2
        
    return 4
    
    # |a-b| = d
    #  axb  = p
    # (a+b)^2 = (a-b)^2 + 4ab
    a_plus_b_squared = d**2 + 4*p
    a_plus_b = a_plus_b_squared ** 0.5
    
    # assuming a > b
    a_minus_b = d
    a = (a_plus_b + a_minus_b)/2
    b = (a_plus_b - a_minus_b)/2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        result = solve(d, p)

        fptr.write(str(result) + '\n')

    fptr.close()
