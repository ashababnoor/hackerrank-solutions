'''
Designer Door Mat
Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().rstrip().split())

h = int(n/2)
for i in range(h):
    design = ".|."*(i*2 + 1)
    print(design.center(m, "-"))

print("WELCOME".center(m, "-"))

for i in reversed(range(h)):
    design = ".|."*(i*2 + 1)
    print(design.center(m, "-"))