'''
Input()
Link: https://www.hackerrank.com/challenges/input/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int, input().split()))
expression = input()

P_x = eval(expression)

print(P_x == k)
