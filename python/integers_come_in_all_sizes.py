'''
Integers Come In All Sizes
Link: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

#  One liner equivalent

print(
    int(input())**int(input()) + int(input())**int(input())
)