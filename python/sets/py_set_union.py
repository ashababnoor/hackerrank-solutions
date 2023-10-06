'''
Set .union() Operation
Link: https://www.hackerrank.com/challenges/py-set-union/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
eng_subs = set(input().rstrip().split())
_ = input()
frn_subs = set(input().rstrip().split())

print(len(eng_subs.union(frn_subs)))