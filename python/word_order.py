'''
Word Order
Link: https://www.hackerrank.com/challenges/word-order/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]

counter = Counter(words)

print(len(set(words)))
print(" ".join([str(value) for key, value in dict(counter).items()]))