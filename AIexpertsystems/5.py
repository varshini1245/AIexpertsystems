from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat}"

def is_valid(state):
    if state.missionaries < 0 or state.cannibals < 0 or state.missionaries > 3 or state.cannibals > 3:
        return False
    if state.missionaries < state.cannibals and state.missionaries > 0:
        return False
    if 3 - state.missionaries < 3 - state.cannibals and state.missionaries < 3:
        return False
    return True

def get_next_states(current_state):
    possible_moves = [
        (2, 0), (0, 2), (1, 1), (1, 0), (0, 1)
    ]
    next_states = []

    for move in possible_moves:
        if current_state.boat == 1:
            new_state = State(
                current_state.missionaries - move[0],
                current_state.cannibals - move[1],
                0
            )
        else:
            new_state = State(
                current_state.missionaries + move[0],
                current_state.cannibals + move[1],
                1
            )
        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def solve_puzzle():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add((current_state.missionaries, current_state.cannibals, current_state.boat))

        if current_state.missionaries == goal_state.missionaries and current_state.cannibals == goal_state.cannibals and current_state.boat == goal_state.boat:
            return path

        for next_state in get_next_states(current_state):
            if (next_state.missionaries, next_state.cannibals, next_state.boat) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

def print_solution(solution):
    if solution:
        print("Solution steps:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

# Solve the river-crossing puzzle
solution = solve_puzzle()
print_solution(solution)
