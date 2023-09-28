'''
Iterables and Iterators
Link: hackerrank.com/challenges/iterables-and-iterators/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input().rstrip())
letters = input().rstrip().split()
k = int(input().rstrip())

letter_to_find = "a"
count = 0

all_combinations = list(combinations("".join(letters), k))
for combination in all_combinations:
    if letter_to_find in combination: count += 1

print(round(count/len(all_combinations), 3))