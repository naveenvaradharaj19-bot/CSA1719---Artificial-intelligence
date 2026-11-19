import math


def alpha_beta(depth, node_index, is_maximizing, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(
                depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth
            )
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned branch at depth {depth + 1}, node {node_index * 2 + i + 1}")
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(
                depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth
            )
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned branch at depth {depth + 1}, node {node_index * 2 + i + 1}")
                break
        return best


if __name__ == "__main__":
    leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
    tree_depth = int(math.log2(len(leaf_scores)))

    optimal_value = alpha_beta(
        0, 0, True, leaf_scores, -math.inf, math.inf, tree_depth
    )
    print(f"Leaf Scores: {leaf_scores}")
    print(f"Optimal Value (Alpha-Beta Pruning): {optimal_value}")
