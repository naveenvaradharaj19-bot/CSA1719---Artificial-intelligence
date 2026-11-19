def astar(graph, heuristic, start, goal):
    open_list = [(0, start)]
    g = {start: 0}
    parent = {}

    while open_list:
        open_list.sort()
        f, node = open_list.pop(0)

        if node == goal:
            path = [node]

            while node in parent:
                node = parent[node]
                path.append(node)

            print("Path:", path[::-1])
            print("Cost:", g[goal])
            return

        for neighbour, cost in graph[node]:
            new_cost = g[node] + cost

            if neighbour not in g or new_cost < g[neighbour]:
                g[neighbour] = new_cost
                parent[neighbour] = node
                open_list.append((new_cost + heuristic[neighbour], neighbour))

    print("No path found")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
