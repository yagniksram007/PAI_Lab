def display_board(board):
    for row in board:
        print('|'.join(row))
    print('---------')

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while not check_winner(board, 'X') and not check_winner(board, 'O') and not check_tie(board):
        display_board(board)

        # Get player move
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if make_move(board, row, col, current_player):
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid input. Row and column must be between 0 and 2.")

    display_board(board)

    if check_winner(board, 'X'):
        print("Player X wins!")
    elif check_winner(board, 'O'):
        print("Player O wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
