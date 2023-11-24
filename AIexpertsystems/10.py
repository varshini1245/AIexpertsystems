from queue import PriorityQueue

# Graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('C', 5), ('D', 9)],
    'B': [('E', 3)],
    'C': [('F', 4)],
    'D': [('G', 7)],
    'E': [],
    'F': [('H', 1)],
    'G': [],
    'H': []
}

def best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))  # Priority queue with the initial node and its cost
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            break

        for next_node, cost in graph[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost  # Best First Search uses the cost as the priority
                frontier.put((priority, next_node))
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
shortest_path, total_cost = best_first_search(graph, start_node, goal_node)
print(f"Shortest Path from {start_node} to {goal_node}: {shortest_path}")
print(f"Total Cost: {total_cost}")
