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