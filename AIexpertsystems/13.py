import random

def objective_function(x):
    # Example objective function (you can replace this with your own function)
    return -x**2 + 20 * x - 10

def hill_climbing():
    current_solution = random.uniform(-10, 10)  # Random initial solution within a range
    step_size = 0.1  # Adjust the step size for climbing

    while True:
        neighbors = [current_solution + step_size, current_solution - step_size]
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]
        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]

        if objective_function(best_neighbor) <= objective_function(current_solution):
            break  # Stop if the current solution is the local maximum
        else:
            current_solution = best_neighbor

    return current_solution, objective_function(current_solution)

# Perform hill climbing
best_solution, best_value = hill_climbing()
print(f"Best Solution: {best_solution}")
print(f"Best Value: {best_value}")
