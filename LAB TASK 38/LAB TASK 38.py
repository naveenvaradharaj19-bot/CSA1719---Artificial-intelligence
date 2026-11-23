# Support Vector Machine

# Training data
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
]

# Class 0 = -1, Class 1 = +1
Y = [-1, -1, -1, 1, 1, 1]

# Initialize weights
w1 = 0.0
w2 = 0.0
b = 0.0

learning_rate = 0.01
regularization = 0.01

# Train SVM
for epoch in range(2000):

    dw1 = regularization * w1
    dw2 = regularization * w2
    db = 0.0

    for i in range(len(X)):

        score = w1 * X[i][0] + w2 * X[i][1] + b

        if Y[i] * score < 1:

            dw1 -= Y[i] * X[i][0]
            dw2 -= Y[i] * X[i][1]
            db -= Y[i]

    w1 -= learning_rate * dw1 / len(X)
    w2 -= learning_rate * dw2 / len(X)
    b -= learning_rate * db / len(X)

# Test data
test = [2, 2]

score = w1 * test[0] + w2 * test[1] + b

if score >= 0:
    result = 1
else:
    result = 0

print("Predicted class:", result)
