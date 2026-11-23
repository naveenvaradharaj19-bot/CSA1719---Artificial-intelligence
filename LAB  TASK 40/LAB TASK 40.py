# Recommendation System

import math

# User-item rating matrix
ratings = [
    [5, 4, 0, 0],
    [4, 0, 5, 0],
    [0, 4, 0, 5],
    [0, 0, 4, 5]
]

# Calculate cosine similarity
def similarity(user1, user2):

    dot = 0
    sum1 = 0
    sum2 = 0

    for i in range(len(user1)):
        dot += user1[i] * user2[i]
        sum1 += user1[i] ** 2
        sum2 += user2[i] ** 2

    if sum1 == 0 or sum2 == 0:
        return 0

    return dot / (math.sqrt(sum1) * math.sqrt(sum2))

# Select user
user = 0

# Find recommendations
best_item = -1
best_score = -1

for item in range(len(ratings[user])):

    # Skip already rated items
    if ratings[user][item] != 0:
        continue

    total = 0
    weight_sum = 0

    for other_user in range(len(ratings)):

        if other_user == user:
            continue

        rating = ratings[other_user][item]

        if rating > 0:
            sim = similarity(
                ratings[user],
                ratings[other_user]
            )

            total += sim * rating
            weight_sum += sim

    if weight_sum > 0:
        score = total / weight_sum

        if score > best_score:
            best_score = score
            best_item = item

print("Recommended item:", best_item + 1)
