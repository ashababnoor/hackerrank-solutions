'''
Map and Lambda Function
Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
'''

from functools import lru_cache

cube = lambda x: x**3

def fibonacci(n):
    fibonacci_list = []
    for _ in range(n):
        fibonacci_list.append(fibonacci_nth_value(_))
    return fibonacci_list

@lru_cache(maxsize=None)
def fibonacci_nth_value(n):
    if n <= 1:
        return n
    else:
        return fibonacci_nth_value(n-1) + fibonacci_nth_value(n-2)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))