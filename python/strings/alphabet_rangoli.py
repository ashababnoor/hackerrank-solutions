'''
Alphabet Rangoli
Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

import string

alphabets = list(string.ascii_lowercase)

def print_rangoli(size):
    length = (size - 1)*4 + 1
    for i in range(size):
        alph_list = list(reversed(alphabets[size-i-1:size]))[:-1] + alphabets[size-i-1:size]
        print("-".join(alph_list).center(length, "-"))
    for i in range(size-1, 0, -1):
        alph_list = list(reversed(alphabets[size-i:size]))[:-1] + alphabets[size-i:size]
        print("-".join(alph_list).center(length, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)