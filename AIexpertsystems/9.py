from itertools import permutations

def total_distance(path, distances):
    total = 0
    for i in range(len(path) - 1):
        total += distances[path[i]][path[i + 1]]
    total += distances[path[-1]][path[0]]  # Return to the starting city
    return total

def tsp_brute_force(cities, distances):
    num_cities = len(cities)
    min_distance = float('inf')
    optimal_path = None

    for perm in permutations(cities):
        distance = total_distance(perm, distances)
        if distance < min_distance:
            min_distance = distance
            optimal_path = perm

    return min_distance, optimal_path

# Example cities and distances (replace with your data)
cities = ['A', 'B', 'C']
distances = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'C': 20},
    'C': {'A': 15, 'B': 20}
}

# Convert distances to a matrix for easier indexing
dist_matrix = {city1: {city2: distances[city1].get(city2, float('inf')) for city2 in cities} for city1 in cities}

min_dist, opt_path = tsp_brute_force(cities, dist_matrix)
print(f"Optimal Path: {opt_path}")
print(f"Minimum Distance: {min_dist}")
