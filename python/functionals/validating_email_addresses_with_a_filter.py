'''
Validating Email Addresses With a Filter
Link: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
'''

import re

def fun(s):
    return bool(re.fullmatch(r"^[A-Za-z0-9\-_]+@[A-Za-z0-9]+\.[A-Za-z]{0,3}", s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)