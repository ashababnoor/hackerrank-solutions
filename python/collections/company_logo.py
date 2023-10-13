'''
Company Logo
Link: https://www.hackerrank.com/challenges/most-commons/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = list(input())
    counter = Counter(s)

    top_three = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))[:3]
        
    for letter, count in sorted(top_three, key=lambda x: (-x[1], x[0])):
        print(letter, count)