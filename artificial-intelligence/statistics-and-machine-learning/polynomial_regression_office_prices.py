'''
Polynomial Regression: Office Prices
Link: https://www.hackerrank.com/challenges/predicting-office-space-price/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

poly_features = PolynomialFeatures(degree=3)
rows_x_poly = poly_features.fit_transform(rows_x)

regressor = LinearRegression()
regressor.fit(rows_x_poly, rows_y)

rows_test_poly = poly_features.transform(rows_test)
results = regressor.predict(rows_test_poly)
for result in results:
    print(result)