import math
from collections import Counter


def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def information_gain(data, feature_index, target_index):
    total_entropy = entropy([row[target_index] for row in data])
    total_rows = len(data)

    subsets = {}
    for row in data:
        key = row[feature_index]
        subsets.setdefault(key, []).append(row)

    weighted_entropy = sum(
        (len(subset) / total_rows) * entropy([row[target_index] for row in subset])
        for subset in subsets.values()
    )
    return total_entropy - weighted_entropy


def build_tree(data, features):
    target_index = len(features)
    labels = [row[target_index] for row in data]

    if len(set(labels)) == 1:
        return labels[0]

    if not features:
        return Counter(labels).most_common(1)[0][0]

    gains = [information_gain(data, i, target_index) for i in range(len(features))]
    best_feature_idx = gains.index(max(gains))
    best_feature = features[best_feature_idx]

    tree = {best_feature: {}}
    remaining_features = features[:best_feature_idx] + features[best_feature_idx + 1 :]

    feature_values = set(row[best_feature_idx] for row in data)
    for value in feature_values:
        subset = [
            row[:best_feature_idx] + row[best_feature_idx + 1 :]
            for row in data
            if row[best_feature_idx] == value
        ]
        tree[best_feature][value] = build_tree(subset, remaining_features)

    return tree


def predict(tree, features, sample):
    if not isinstance(tree, dict):
        return tree

    root_feature = next(iter(tree))
    feature_idx = features.index(root_feature)
    sample_val = sample[feature_idx]

    if sample_val in tree[root_feature]:
        return predict(tree[root_feature][sample_val], features, sample)
    return "Unknown"


if __name__ == "__main__":
    feature_names = ["Outlook", "Temperature", "Humidity", "Wind"]
    dataset = [
        ["Sunny", "Hot", "High", "Weak", "No"],
        ["Sunny", "Hot", "High", "Strong", "No"],
        ["Overcast", "Hot", "High", "Weak", "Yes"],
        ["Rain", "Mild", "High", "Weak", "Yes"],
        ["Rain", "Cool", "Normal", "Weak", "Yes"],
        ["Rain", "Cool", "Normal", "Strong", "No"],
        ["Overcast", "Cool", "Normal", "Strong", "Yes"],
        ["Sunny", "Mild", "High", "Weak", "No"],
        ["Sunny", "Cool", "Normal", "Weak", "Yes"],
        ["Rain", "Mild", "Normal", "Weak", "Yes"],
        ["Sunny", "Mild", "Normal", "Strong", "Yes"],
        ["Overcast", "Mild", "High", "Strong", "Yes"],
        ["Overcast", "Hot", "Normal", "Weak", "Yes"],
        ["Rain", "Mild", "High", "Strong", "No"],
    ]

    decision_tree = build_tree(dataset, feature_names)
    print("Generated Decision Tree:")
    print(decision_tree)

    test_sample = ["Sunny", "Cool", "High", "Strong"]
    prediction = predict(decision_tree, feature_names, test_sample)
    print(f"\nPrediction for {test_sample}: Play Tennis = {prediction}")
