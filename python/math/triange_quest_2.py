'''
Triangle Quest 2
Link: https://www.hackerrank.com/challenges/python-quest-2/problem
'''

for i in range(1, int(input())+1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i, (11**(i+2)) - (11**i)*(10**(i-1))*i + 10**i)