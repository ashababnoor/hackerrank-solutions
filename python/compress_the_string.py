'''
Compress the String!
Link: https://www.hackerrank.com/challenges/compress-the-string/problem
'''

from itertools import groupby

string = input().rstrip()
output = ""

for key, values in groupby(string):
    output += f"({len(list(values))}, {list(key)[0]}) "
    
print(output)

