def is_safe(board, row, col, N):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_queens(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_queens(board, 0, N):
        print("No solution exists")
        return False

    print_solution(board, N)
    return True

# Example: Solve the 8-Queens problem
n = 8
solve_n_queens(n)
