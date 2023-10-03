'''
Hex Color Code
Link: https://www.hackerrank.com/challenges/hex-color-code/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

n = int(input())
all_lines = ""
for _ in range(n): 
    all_lines += input().rstrip() + "\n"

color_finder = r'color:\s+#([0-9a-fA-f]{3}|[0-9a-fA-F]{6})'
hex_finder = r'#([0-9a-fA-f]{3}|[0-9a-fA-F]{6})'

color_lines = re.findall(color_finder, all_lines)

for color_line in color_lines:
    color_codes = re.findall(hex_finder, color_line)
    for color_code in color_codes: 
        print(color_code)