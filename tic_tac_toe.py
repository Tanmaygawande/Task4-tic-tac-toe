import math


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(cell in ("X", "O") for cell in board):
        return "draw"

    return None


def minimax(board, maximizing):
    result = winner(board)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] not in ("X", "O"):
                old = board[i]
                board[i] = "O"
                best = max(best, minimax(board, False))
                board[i] = old
        return best

    best = math.inf
    for i in range(9):
        if board[i] not in ("X", "O"):
            old = board[i]
            board[i] = "X"
            best = min(best, minimax(board, True))
            board[i] = old
    return best


def computer_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] not in ("X", "O"):
            old = board[i]
            board[i] = "O"
            score = minimax(board, False)
            board[i] = old

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


board = [str(i) for i in range(1, 10)]

print("Tic-Tac-Toe AI")
print("You are X. Computer is O.")

while True:
    print_board(board)

    try:
        move = int(input("Choose a position (1-9): ")) - 1
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if move < 0 or move > 8 or board[move] in ("X", "O"):
        print("That position is not available.")
        continue

    board[move] = "X"

    result = winner(board)
    if result:
        break

    ai_move = computer_move(board)
    board[ai_move] = "O"

    result = winner(board)
    if result:
        break

print_board(board)

if result == "draw":
    print("It's a draw.")
else:
    print("Winner:", result)
