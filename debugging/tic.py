#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Kthen lojtarin fitues

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # Asnjë fitues ende

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None
    moves = 0

    while not winner and moves < 9:  # Loja përfundon kur kemi fitues ose tabela është plot
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:  # Kontrolli për input të vlefshëm
            if board[row][col] == " ":
                board[row][col] = player
                winner = check_winner(board)
                player = "O" if player == "X" else "X"
                moves += 1
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input! Please enter numbers between 0 and 2.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
