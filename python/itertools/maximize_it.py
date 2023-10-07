'''
Maximize It!
Link: https://www.hackerrank.com/challenges/maximize-it/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

def square_sum(values: list) -> int:
    return sum(num**2 for num in values)

def custom_modder(values: list, m: int) -> int:
    return sum((num % m)**2 % m for num in values) % m

k, m = map(int, input().rstrip().split())

lists = []
for _ in range(k):
    ignore, *inputs = map(int, input().rstrip().split())
    lists.append(list(inputs))

max_ = float("-inf")
for values in product(*lists):
    s = custom_modder(values, m)
    if s > max_: max_ = s

print(max_)