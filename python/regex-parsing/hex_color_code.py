'''
Hex Color Code
Link: https://www.hackerrank.com/challenges/hex-color-code/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

n = int(input())
lines = []
for _ in range(n): 
    lines.append(input().rstrip())

property_finder = r'.*:.*;'
hex_finder = r'(#[0-9a-fA-f]{6}|#[0-9a-fA-F]{3})'

for line in lines:
    if len(re.findall(property_finder, line)) > 0:
        
        color_codes = re.findall(hex_finder, line)
        
        for color_code in color_codes: 
            print(color_code)