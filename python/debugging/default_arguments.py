'''
Default Arguments
Link: https://www.hackerrank.com/challenges/default-arguments/problem
'''

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n=1, stream=EvenStream()):
    # using __init__() gives the wrong result here
    stream = stream.__class__()
    for _ in range(n):
        print(stream.get_next())


# alternative method to avoid default argument mutation
# read more: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments 

def print_from_stream(n=1, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
