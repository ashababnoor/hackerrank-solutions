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