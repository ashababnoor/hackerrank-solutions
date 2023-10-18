'''
Any or All
Link: https://www.hackerrank.com/challenges/any-or-all/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]
    
n = int(input())
nums = list(map(int, input().split()))

palindrome_check = []
positive_check = []

for num in nums:
    palindrome_check.append(is_palindrome(num)==True)
    positive_check.append(num>0)

print(all(positive_check) and any(palindrome_check))