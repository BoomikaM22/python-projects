def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(len(board))):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    turns = 0

    while turns < 9:
        print_board(board)

        print(f"Player {current_player}'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Try again.")
            continue

        if board[row][col] == " ":
            board[row][col] = current_player
            turns += 1

            if check_winner(board):
                print_board(board)0
                print(f"Player {current_player} wins!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

    if turns == 9:
        print_board(board)
        print("It's a tie!")


tic_tac_toe()
