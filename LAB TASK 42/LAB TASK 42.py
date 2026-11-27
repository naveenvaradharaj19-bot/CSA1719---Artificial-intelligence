
# K-Means Clustering

data = [[1, 2], [2, 1], [3, 2],
        [8, 9], [9, 8], [10, 9]]

centroids = [[1, 2], [8, 9]]

for iteration in range(5):

    cluster1 = []
    cluster2 = []

    for point in data:

        d1 = ((point[0] - centroids[0][0]) ** 2 +
              (point[1] - centroids[0][1]) ** 2)

        d2 = ((point[0] - centroids[1][0]) ** 2 +
              (point[1] - centroids[1][1]) ** 2)

        if d1 <= d2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    centroids[0] = [
        sum(p[0] for p in cluster1) / len(cluster1),
        sum(p[1] for p in cluster1) / len(cluster1)
    ]

    centroids[1] = [
        sum(p[0] for p in cluster2) / len(cluster2),
        sum(p[1] for p in cluster2) / len(cluster2)
    ]

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Centroids:", centroids)
