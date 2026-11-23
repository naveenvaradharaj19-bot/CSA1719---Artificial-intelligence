# Principal Component Analysis

import math

# Dataset
data = [
    [2, 4],
    [3, 5],
    [4, 6],
    [5, 7]
]

n = len(data)

# Calculate mean
mean_x = sum(row[0] for row in data) / n
mean_y = sum(row[1] for row in data) / n

# Center the data
centered = []

for row in data:
    centered.append([
        row[0] - mean_x,
        row[1] - mean_y
    ])

# Calculate covariance values
cov_xx = sum(row[0] ** 2 for row in centered) / n
cov_yy = sum(row[1] ** 2 for row in centered) / n
cov_xy = sum(row[0] * row[1] for row in centered) / n

# Calculate principal component direction
angle = 0.5 * math.atan2(
    2 * cov_xy,
    cov_xx - cov_yy
)

pc1_x = math.cos(angle)
pc1_y = math.sin(angle)

# Project data onto first principal component
reduced = []

for row in centered:
    value = row[0] * pc1_x + row[1] * pc1_y
    reduced.append([round(value, 2)])

print("Reduced data:")
for row in reduced:
    print(row)

print("Reduced dimensions:",
      len(reduced), "x", len(reduced[0]))
