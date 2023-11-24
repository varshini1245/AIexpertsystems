import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                cells.append((i, j))
    return cells

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return 1 if winner == 'O' else -1 if winner == 'X' else 0

    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ' '
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                best_move = find_best_move(board)
                board[best_move[0]][best_move[1]] = 'O'
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
        else:
            print("That spot is already taken! Try again.")

# Start the game
play_game()
