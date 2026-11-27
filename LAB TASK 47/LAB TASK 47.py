# Hyperparameter Tuning

# Training data
X = [1, 2, 3, 6, 7, 8]
Y = [0, 0, 0, 1, 1, 1]

# Test data
test_x = [2, 7]
test_y = [0, 1]

best_k = 1
best_accuracy = 0

for k in [1, 3, 5]:

    correct = 0

    for i in range(len(test_x)):

        distances = []

        for j in range(len(X)):
            distance = abs(test_x[i] - X[j])
            distances.append((distance, Y[j]))

        distances.sort()

        neighbors = distances[:k]

        count0 = sum(1 for item in neighbors
                     if item[1] == 0)

        count1 = sum(1 for item in neighbors
                     if item[1] == 1)

        if count0 > count1:
            prediction = 0
        else:
            prediction = 1

        if prediction == test_y[i]:
            correct += 1

    accuracy = correct / len(test_x)

    print("K =", k, "Accuracy =", accuracy)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

print("Best K:", best_k)
print("Best accuracy:", best_accuracy)
