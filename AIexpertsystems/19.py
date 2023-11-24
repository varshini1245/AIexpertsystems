import math
import random

# Function to calculate the total distance of a path
def total_distance(path, distances):
    total = 0
    for i in range(len(path) - 1):
        total += distances[path[i]][path[i + 1]]
    total += distances[path[-1]][path[0]]  # Return to the starting city
    return total

# Function to generate initial random solution
def initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)

# Simulated Annealing algorithm
def simulated_annealing(distances, temperature=10000, cooling_rate=0.003, num_iterations=10000):
    num_cities = len(distances)
    current_solution = initial_solution(num_cities)
    best_solution = list(current_solution)
    
    while temperature > 1:
        for i in range(num_iterations):
            # Swap two random cities
            index1, index2 = random.sample(range(num_cities), 2)
            new_solution = list(current_solution)
            new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
            
            # Calculate the energy (total distance) of the new solution
            current_energy = total_distance(current_solution, distances)
            new_energy = total_distance(new_solution, distances)
            
            # Decide whether to accept the new solution
            if new_energy < current_energy or random.random() < math.exp((current_energy - new_energy) / temperature):
                current_solution = list(new_solution)
                if new_energy < total_distance(best_solution, distances):
                    best_solution = list(new_solution)
        
        # Cool down the temperature
        temperature *= 1 - cooling_rate
    
    return best_solution, total_distance(best_solution, distances)

# Example distances between cities (replace this with your own distances)
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Running the simulated annealing algorithm
best_path, shortest_distance = simulated_annealing(distances)

print("Best Path:", best_path)
print("Shortest Distance:", shortest_distance)
