import math


def minimax(depth, node_index, is_maximizing, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, scores, max_depth)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, scores, max_depth)
            best = min(best, val)
        return best


if __name__ == "__main__":
    leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
    tree_depth = int(math.log2(len(leaf_scores)))

    optimal_value = minimax(0, 0, True, leaf_scores, tree_depth)
    print(f"Leaf Scores: {leaf_scores}")
    print(f"Optimal Value (Minimax): {optimal_value}")
