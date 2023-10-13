'''
ginortS
Link: https://www.hackerrank.com/challenges/ginorts/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def custom_value(char: str) -> int:
    if char.islower():
        return 0
    elif char.isupper():
        return 1
    elif char.isdigit():
        if int(char) % 2 != 0:
            return 2
        else:
            return 3
    else: 
        return 99
        
string = input().rstrip()
sorted_string = sorted(string, key=lambda x: (custom_value(x), x))

print("".join(sorted_string))