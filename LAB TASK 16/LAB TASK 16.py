# Feed Forward Neural Network

import math

# Input data
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Feed Forward Process
def feed_forward(x):

    # Hidden layer
    h1 = sigmoid(20 * x[0] + 20 * x[1] - 10)
    h2 = sigmoid(20 * x[0] + 20 * x[1] - 30)

    # Output layer
    output = sigmoid(20 * h1 - 20 * h2 - 10)

    return output

# Display output
print("Feed Forward Neural Network Output:")

for x in X:
    output = feed_forward(x)
    print(round(output, 4))

print("\nPredicted Values:")

for x in X:
    output = feed_forward(x)

    if output > 0.5:
        print(1)
    else:
        print(0)
