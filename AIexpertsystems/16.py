import math

# Constants for representing players and empty cells
X = 'X'
O = 'O'
EMPTY = None

# Function to check for a winner
def winner(board):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

# Function to check if the board is full
def board_full(board):
    return all(all(cell is not None for cell in row) for row in board)

# Function to get available moves
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

# Minimax with Alpha-Beta pruning
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    # Base cases: check for terminal state or depth limit
    current_winner = winner(board)
    if current_winner == X:
        return -1
    elif current_winner == O:
        return 1
    elif board_full(board) or depth == 0:
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = O
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = X
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Example usage
if __name__ == "__main__":
    # Initial empty 3x3 board
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    # Calling the minimax function with alpha-beta pruning
    result = minimax_alpha_beta(board, 9, -math.inf, math.inf, True)
    print("The result of the game is:", result)
