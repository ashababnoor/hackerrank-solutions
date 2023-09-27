'''
No Idea!
Link: https://www.hackerrank.com/challenges/no-idea/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

i1 = input().rstrip().split()
n = int(i1[0])
m = int(i1[1])

arr = input().rstrip().split()
a = set(input().rstrip().split())
b = set(input().rstrip().split())

happiness = 0
for _ in arr:
    if _ in a: happiness += 1
    if _ in b: happiness -= 1
    
print(happiness)
