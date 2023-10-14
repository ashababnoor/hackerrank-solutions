'''
Validating Credit Card Numbers
Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def credit_card_validity(card: str) -> str:
    valid = "Valid"
    invalid = "Invalid"

    # If it doesn't start with 4, 5, 6
    if len(re.findall(r"^[^456]", card)) != 0:
        return invalid

    # If consecutive digits are repeating 4 or more times
    if len(re.findall(r"(\d)\1\1\1", re.sub(r"\-", "", card))) != 0:
        return invalid

    # If there is anything other than digits and hash (-)
    if len(re.findall(r"[^\d\-]", card)) != 0:
        return invalid

    # If there isn't exactly 16 digits
    if len(re.findall(r"^\d{16}$", re.sub(r"\-", "", card))) != 1:
        return invalid

    # If numbers aren't divided into equal groups of 4
    if len(re.findall(r"\-", card)) != 0:
        if len(re.findall(r"^\d{4}-\d{4}-\d{4}-\d{4}$", card)) != 1:
            return invalid

    return valid


n = int(input().rstrip())
for _ in range(n):
    card = input()
    print(credit_card_validity(card))