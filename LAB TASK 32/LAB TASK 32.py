# Linear Regression

# Training data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

# Calculate sums
sum_x = sum(x)
sum_y = sum(y)

sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(x[i] * x[i] for i in range(n))

# Calculate slope
m = (n * sum_xy - sum_x * sum_y) / \
    (n * sum_x2 - sum_x * sum_x)

# Calculate intercept
c = (sum_y - m * sum_x) / n

# Predict value
new_x = 6
prediction = m * new_x + c

print("Slope:", m)
print("Intercept:", c)
print("Predicted value:", prediction)
