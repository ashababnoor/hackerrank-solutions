'''
Correlation and Regression Lines - A Quick Recap #1
Link: https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem 
'''

import numpy as np

phy_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
hist_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

phy_arr = np.array(phy_scores, dtype=float)
hist_arr = np.array(hist_scores, dtype=float)

'''
Karl Pearson Correlation coefficient:
r = summation(
    (x - x.mean) * (y - y.mean)
) / (
    sqrt(
        summation((x - x.mean)^2)
    ) * sqrt (
        summation((y - y.mean)^2)
    )
)
'''

dividend = np.sum(
    (phy_arr - np.mean(phy_arr)) * (hist_arr - np.mean(hist_arr))
)

divisor = np.sqrt(
    np.sum(np.square(phy_arr - np.mean(phy_arr)))
) * np.sqrt(
    np.sum(np.square(hist_arr - np.mean(hist_arr)))
)

r = dividend / divisor

print(f"Pearson Correlation Coefficient: {r:.3f}")


# Alternate method
# ----------------

correlation_matrix = np.corrcoef(phy_arr, hist_arr)

# The correlation coefficient is at position (0, 1) or (1, 0) in the correlation matrix
correlation_coefficient = correlation_matrix[0, 1]

print(f"Pearson Correlation Coefficient: {correlation_coefficient}")