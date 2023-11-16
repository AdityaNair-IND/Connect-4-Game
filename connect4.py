"""
####################################
#     Connect4 by Aditya Nair      #
#  Made with 💝 in India 🧡🤍💚  #
####################################

"""

import os
import random
import sys

# player colors
colors = ['\033[91m', '\033[92m', '\033[93m']
random.shuffle(colors)

player_colors = {'θ': colors[0], 'Ø': colors[1]}
reset_colors = '\033[0m'

# disc representation and display board
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for row in board:
        for disc in row:
            if disc in player_colors:
                print(f"{player_colors[disc]}{disc}{reset_colors}", end='|')
            else:
                print(f"{disc}|", end='')
        print('\n' + '-' * 14)
    print(' 1 2 3 4 5 6 7')


# player move
def player_move(board, column, player):
    if column == -1 or board[0][column] != ' ':
        print("Invalid column. Choose another column.")
        return False

    for i in range(5, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return True

# check win
def check_win(board, player):
    # check for horizontal win
    for row in board:
        if ''.join(row).count(player * 4) > 0:
            return True

    # check for vertical win
    for col in range(7):
        if ''.join([board[row][col] for row in range(6)]).count(player * 4) > 0:
            return True

    # check for diagonal win
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == player:
                return True

            if board[i][j + 3] == board[i + 1][j + 2] == board[i + 2][j + 1] == board[i + 3][j] == player:
                return True

    return False

# main game loop
if __name__ == "__main__":
    while True:
        board = [[' ' for _ in range(7)] for _ in range(6)]
        player_turn = 'θ'

        while True:
            display_board(board)

            try:
                move = input(f"Player {player_turn}, choose a column (1-7), or press 'q' to quit: ")
                if move.lower() == 'q':
                    sys.exit()  # Exit the program

                column = int(move) - 1 if 0 <= int(move) - 1 < 7 else -1
                player_move_result = player_move(board, column, player_turn)

                if not player_move_result:
                    print('Invalid move. Try again! or press Q to quit.')
                    continue

                if check_win(board, player_turn):
                    display_board(board)
                    print(f"🎉 Congratulations, Player {player_turn} wins!")
                    break

                player_turn = 'Ø' if player_turn == 'θ' else 'θ'

            except (ValueError, IndexError):
                print('Invalid move. Try again! or press Q to quit.')

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

# https://github.com/AdityaNair-IND 