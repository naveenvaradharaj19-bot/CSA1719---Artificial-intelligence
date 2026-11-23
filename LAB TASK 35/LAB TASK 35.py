# Decision Tree Classification

# Training data
X = [1, 2, 3, 6, 7, 8]
Y = [0, 0, 0, 1, 1, 1]

# Find the best split
best_threshold = 0
best_gini = 1

for i in range(len(X) - 1):
    threshold = (X[i] + X[i + 1]) / 2

    left = []
    right = []

    for j in range(len(X)):
        if X[j] <= threshold:
            left.append(Y[j])
        else:
            right.append(Y[j])

    # Calculate Gini impurity
    gini_left = 0
    gini_right = 0

    if len(left) > 0:
        p = left.count(0) / len(left)
        gini_left = 1 - p * p - (1 - p) * (1 - p)

    if len(right) > 0:
        p = right.count(0) / len(right)
        gini_right = 1 - p * p - (1 - p) * (1 - p)

    gini = (len(left) * gini_left +
            len(right) * gini_right) / len(X)

    if gini < best_gini:
        best_gini = gini
        best_threshold = threshold

# Predict class
test_value = 2

if test_value <= best_threshold:
    result = 0
else:
    result = 1

print("Best threshold:", best_threshold)
print("Predicted class:", result)
