from collections import deque

def solve(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        i = state.index(0)
        moves = []

        if i >= 3:
            moves.append(i - 3)
        if i < 6:
            moves.append(i + 3)
        if i % 3 != 0:
            moves.append(i - 1)
        if i % 3 != 2:
            moves.append(i + 1)

        for j in moves:
            new = list(state)
            new[i], new[j] = new[j], new[i]
            queue.append((tuple(new), path + [state]))

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = solve(start, goal)

if result:
    for step in result:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution")
