'''
Correlation and Regression Lines - A Quick Recap #2
Link: https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem 
'''

import numpy as np

phy_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
hist_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

phy_arr = np.array(phy_scores, dtype=float)
hist_arr = np.array(hist_scores, dtype=float)

'''
The slope of the line of regression:
slope(b) = summation(
    (x - x.mean) * (y - y.mean)
) / (
    summation((x - x.mean)^2) 
)

x = independent variable
y = dependent variable
'''

dividend = np.sum(
    (phy_arr - np.mean(phy_arr)) * (hist_arr - np.mean(hist_arr))
)

divisor = np.sum(np.square(phy_arr - np.mean(phy_arr)))

slope = dividend / divisor

print(f"Slope: {slope:.3f}")