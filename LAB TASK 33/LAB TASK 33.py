# K-Nearest Neighbors Classification

# Training data
X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 8]]

y = [0, 0, 0, 1, 1, 1]

# Test data
test = [2, 2]

# Calculate distances
distances = []

for i in range(len(X)):
    distance = ((X[i][0] - test[0]) ** 2 +
                (X[i][1] - test[1]) ** 2) ** 0.5

    distances.append((distance, y[i]))

# Sort distances
distances.sort()

# Select 3 nearest neighbors
neighbors = distances[:3]

# Count classes
count0 = 0
count1 = 0

for neighbor in neighbors:
    if neighbor[1] == 0:
        count0 += 1
    else:
        count1 += 1

# Find predicted class
if count0 > count1:
    result = 0
else:
    result = 1

print("Predicted class:", result)
