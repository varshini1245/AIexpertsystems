from collections import deque

# Function to print the current state of the puzzle
def print_puzzle(puzzle):
    for row in puzzle:
        print(' '.join(map(str, row)))
    print('\n')

# Function to find the empty space in the puzzle
def find_empty(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Function to generate all possible moves from a given state
def generate_moves(puzzle):
    empty_i, empty_j = find_empty(puzzle)
    moves = []

    # Define possible moves (up, down, left, right)
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in possible_moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[empty_i][empty_j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[empty_i][empty_j]
            moves.append(new_puzzle)

    return moves

# Function to solve the sliding puzzle
def solve_puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state

    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return path

        for move in generate_moves(current_state):
            if tuple(map(tuple, move)) not in visited:
                queue.append((move, path + [move]))

    return None

# Example initial state
initial_puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]

print("Initial State:")
print_puzzle(initial_puzzle)

# Solve the puzzle
solution = solve_puzzle(initial_puzzle)

if solution:
    print("Solution Steps:")
    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")
