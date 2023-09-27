'''
Merge the Tools!
Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    n = len(string)
    sub_strings = ["".join(list(set(string[i*k:i*k+k]))) for i in range(int(n/k))]
    for sub_string in sub_strings:
        print(sub_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)