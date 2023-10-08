'''
Multiple Linear Regression: Predicting House Prices
Link: https://www.hackerrank.com/challenges/predicting-house-prices/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.linear_model import LinearRegression

f, n = map(int, input().split())
rows_x = []
rows_y = []

for _ in range(n):
    *x, y = list(map(float, input().split()))
    rows_x.append(x)
    rows_y.append(y)
    
t = int(input())
rows_test = []
for _ in range(t):
    rows_test.append(list(map(float, input().split())))

regressor = LinearRegression()
regressor.fit(rows_x, rows_y)

results = regressor.predict(rows_test)
for result in results:
    print(result)
    

# Pure Numpy Solution
import numpy as np

F, H = map(int, input().split())
x, y = np.empty((H, F + 1)), np.empty(H)

for h in range(H):
    fs = list(map(np.float32, input().split()))
    x[h], y[h] = fs[:-1] + [1], fs[-1]

w = np.linalg.inv(x.T @ x) @ x.T @ y
    
for t in range(int(input())):
    print((np.array([[*map(np.float32, input().split()), 1]]) @ w)[0])