from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        if state in visited:
            continue

        visited.add(state)
        m, c, boat = state

        for x, y in moves:
            if boat == 1:
                new = (m-x, c-y, 0)
            else:
                new = (m+x, c+y, 1)

            nm, nc, nb = new

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):
                    if new not in visited:
                        queue.append((new, path + [state]))

solve()
