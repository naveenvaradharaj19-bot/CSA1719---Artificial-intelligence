# Neural Network for Image Classification

import math

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Training images: 4 pixels each
X = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# 0 = Top row, 1 = Bottom row
Y = [0, 0, 0, 1, 1, 1]

# Initialize weights
weights = [0.0, 0.0, 0.0, 0.0]
bias = 0.0

learning_rate = 0.5

# Train neural network
for epoch in range(1000):
    for i in range(len(X)):
        total = bias

        for j in range(4):
            total += weights[j] * X[i][j]

        output = sigmoid(total)
        error = output - Y[i]

        for j in range(4):
            weights[j] -= learning_rate * error * X[i][j]

        bias -= learning_rate * error

# Test image
test_image = [1, 1, 0, 0]

total = bias

for j in range(4):
    total += weights[j] * test_image[j]

output = sigmoid(total)

if output < 0.5:
    print("Predicted class: Top row")
else:
    print("Predicted class: Bottom row")
