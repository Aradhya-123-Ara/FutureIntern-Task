def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    if all(board[i][i] == player for i in range(3)):  # Main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Choose a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("Cell already taken. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")

def play_game():
    while True:
        board = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]
        current_player = 'X'
        print("Welcome to Tic-Tac-Toe!")
        print_board(board)

        while True:
            row, col = get_move(current_player, board)
            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw! 🤝")
                break
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask to play again
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing! 👋")
            break

# Run the game
play_game()
