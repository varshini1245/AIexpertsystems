import heapq

# Graph represented as an adjacency list with edge costs
graph = {
    'A': {'B': 2, 'C': 5, 'D': 9},
    'B': {'E': 3},
    'C': {'F': 4},
    'D': {'G': 7},
    'E': {},
    'F': {'H': 1},
    'G': {},
    'H': {}
}

def heuristic(node, goal):
    # Replace this heuristic with an appropriate function for your problem
    # Here, it's a simple Manhattan distance heuristic for demonstration purposes
    node_coords = {'A': (0, 0), 'B': (1, 1), 'C': (2, 1), 'D': (2, 0), 'E': (2, 2), 'F': (3, 1), 'G': (3, 0), 'H': (4, 1)}
    goal_coords = {'A': (4, 1), 'B': (4, 1), 'C': (4, 1), 'D': (4, 1), 'E': (4, 1), 'F': (4, 1), 'G': (4, 1), 'H': (4, 1)}
    node_x, node_y = node_coords[node]
    goal_x, goal_y = goal_coords[goal]
    return abs(node_x - goal_x) + abs(node_y - goal_y)

def astar(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))  # Priority queue with the initial node and its cost
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node == goal:
            break

        for next_node, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)  # A* uses g + h as priority
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current_node

    # Reconstruct the path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]

# Example usage:
start_node = 'A'
goal_node = 'H'
shortest_path, total_cost = astar(graph, start_node, goal_node)
print(f"Shortest Path from {start_node} to {goal_node}: {shortest_path}")
print(f"Total Cost: {total_cost}")
