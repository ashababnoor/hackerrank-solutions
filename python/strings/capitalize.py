'''
Capitilize!
Link: https://www.hackerrank.com/challenges/capitalize/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    '''
    Capitalizes the first letter of all words in sentence.
    Example: 
        "john doe" --> "John Doe"
        "john 0doe" --> "John 0doe"
    
    Note: s.title() fails for a lot of test cases for this specific problem
    '''
    return s[0].title() + "".join([char.title() if s[ind] == " " else char for ind, char in enumerate(s[1:])])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
