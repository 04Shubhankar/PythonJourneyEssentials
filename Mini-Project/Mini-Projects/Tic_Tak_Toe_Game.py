def print_board(board):
    """Prints the current state of the tic tac toe board."""
    for row in board:
        print("|".join(cell if cell != "" else " " for cell in row))  # Handles empty cells
        print("-" * 9)

def check_win(board, player):
    """Checks if the given player has won the game.

    Args:
        board: The current state of the tic tac toe board.
        player: The player to check for victory.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def play_tic_tac_toe():
    """Plays a tic tac toe game."""

    board = [["", "", ""], ["", "", ""], ["", "", ""]]  # Use empty strings
    players = ["X", "O"]
    current_player = 0
    game_over = False

    while not game_over:
        player = players[current_player]
        print(f"It's {player}'s turn.")

        position = int(input("Enter a position (1-9): ")) - 1

        # Check if the position is valid and empty
        if board[position // 3][position % 3] == "":
            board[position // 3][position % 3] = player
        else:
            print("That position is already taken. Try again.")
            continue

        print_board(board)

        # Check for a win
        if check_win(board, player):
            print(f"{player} wins!")
            game_over = True
        # Check for a tie
        elif all(cell != "" for row in board for cell in row):
            print("It's a tie!")
            game_over = True

        # Switch players
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
