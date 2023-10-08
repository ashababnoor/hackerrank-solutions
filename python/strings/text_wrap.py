'''
Text Wrap
Link: https://www.hackerrank.com/challenges/text-wrap/problem
'''

import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

# alternate method using built-in function
def wrap_(string, max_width):
    result = textwrap.fill(string, max_width)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)