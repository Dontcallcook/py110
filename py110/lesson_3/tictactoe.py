import random
import os
import time

EMPTY_MARKER = " "
PLAYER_MARKER = "X"
COMPUTER_MARKER = "O"
WIN_REQ = 5
WINNING_MOVES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
    ]

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def prompt(message):
    print(f"---> {message}")

def join_or(lst, delimiter=", ", fin_delimiter="or"):
    if len(lst) == 0:
        return lst
    if len(lst) == 1:
        return str(lst[0])
    if len(lst) == 2:
        return str(lst[0]) + " " + fin_delimiter + " " + str(lst[1])
    if len(lst) > 2:
        leading_items = delimiter.join([str(item) for item in lst[0:-1]])
        return f'{leading_items}{delimiter}{fin_delimiter} {str(lst[-1])}'

    return None

def display_welcome():
    prompt("Welcome to Tic Tac Toe!")
    prompt("")
    prompt("Press 'Enter' to start")
    input()
    clear_screen()

def display_turn_choice():
    prompt("Choose the turn order:")
    prompt("")
    prompt("1) Player first")
    prompt("2) Player second")
    prompt("3) Random")

def choose_turn(current_player):
    display_turn_choice()
    turn_choice = input()

    while turn_choice not in ['1', '2', '3']:
        clear_screen()
        prompt("That's not a valid choice!")
        time.sleep(0.5)
        clear_screen()
        display_turn_choice()
        turn_choice = input()

    if turn_choice == '1':
        turn_choice = current_player[0]
    if turn_choice == '2':
        turn_choice = current_player[1]
    if turn_choice == '3':
        turn_choice = random.choice(current_player)

    return turn_choice

def init_board():
    return {key: EMPTY_MARKER for key in range(1, 10)}

def display_board(board):
    clear_screen()
    prompt(f'You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}')
    prompt('')
    prompt('       |       |       ')
    prompt(f'   {board[1]}   |   {board[2]}   |   {board[3]}   ')
    prompt('       |       |       ')
    prompt('-------+-------+-------')
    prompt('       |       |       ')
    prompt(f'   {board[4]}   |   {board[5]}   |   {board[6]}   ')
    prompt('       |       |       ')
    prompt('-------+-------+-------')
    prompt('       |       |       ')
    prompt(f'   {board[7]}   |   {board[8]}   |   {board[9]}   ')
    prompt('       |       |       ')
    prompt('')

def available_squares(board):
    return [str(key) for key in board.keys()
            if board[key] == EMPTY_MARKER]

def valid_choice(player_choice, available):
    try:
        int(player_choice)
    except ValueError:
        return False

    if player_choice not in available:
        return False

    return True

def get_player_choice(board):
    prompt("Choose your move!")
    prompt(f"Available squares: {join_or(available_squares(board))}")
    player_choice = input().strip()

    while not valid_choice(player_choice, available_squares(board)):
        prompt("That's not a valid move!")
        prompt(f"Choose from the available squares: {join_or(available_squares(board))}")
        player_choice = input().strip()

    board[int(player_choice)] = PLAYER_MARKER

def get_computer_choice(board):
    if len(available_squares(board)) == 0:
        return

    turn_marker = 0
    computer_choice = None
    for sublist in WINNING_MOVES:
        computer_choice = computer_response(sublist, board, COMPUTER_MARKER)
        if computer_choice:
            turn_marker += 1
            break

    if not computer_choice:
        for sublist in WINNING_MOVES:
            computer_choice = computer_response(sublist, board, PLAYER_MARKER)
            if computer_choice:
                turn_marker += 1
                break

    if not computer_choice:
        if board[5] == ' ' and turn_marker > 0:
            computer_choice = 5
        else:
            computer_choice = int(random.choice(available_squares(board)))
            turn_marker += 1

    board[computer_choice] = COMPUTER_MARKER

def computer_response(sublist, board, marker):
    occupied_squares = [board[square] for square in sublist]

    if occupied_squares.count(marker) == 2:
        for square in sublist:
            if board[square] == ' ':
                return square

    return None

def board_full(board):
    return len(available_squares(board)) == 0

def check_game_finished(board):
    if board_full(board) or someone_won(board):
        if someone_won(board):
            clear_screen()
            flash_message(f"{detect_game_winner(board)} wins!")
            return True

        flash_message("It's a tie!")
        return True

    return False

def flash_message(message):
    for _ in range(1, 10):
        prompt(message)
        prompt("")
    clear_screen()
    prompt(message.center(24))
    time.sleep(0.5)
    clear_screen()
    time.sleep(0.5)
    prompt(message.center(24))
    time.sleep(0.5)
    clear_screen()
    time.sleep(0.5)
    prompt(message.center(24))
    time.sleep(0.5)

def someone_won(board):
    return bool(detect_game_winner(board))

def detect_game_winner(board):
    computer_moves = [square for square, marker in board.items() if marker == "O"]
    player_moves = [square for square, marker in board.items() if marker == "X"]

    for sublist in WINNING_MOVES:
        if all(square in computer_moves for square in sublist):
            return "Computer"
        if all(square in player_moves for square in sublist):
            return "Player"

    return None

def play_again_check():
    prompt("")
    prompt("Would you like to play again? Y/N")
    choice = input().lower().strip()

    while choice not in ['y', 'yes', 'n', 'no']:
        prompt("That's not a valid choice!")
        prompt("Please enter Y/N")
        choice = input().lower().strip()

    if choice[0] == "n":
        return False
    clear_screen()
    prompt("Great! Get ready for the next round...")
    return True

def choose_square(player, board):
    if player == 'player':
        get_player_choice(board)
    else:
        get_computer_choice(board)

def alternate_player(player):
    if player == 'player':
        return 'computer'

    return 'player'

def play_tic_tac_toe():
    scores = {'computer': 0, 'player': 0}
    board = {
    1: EMPTY_MARKER, 2: EMPTY_MARKER, 3: EMPTY_MARKER,
    4: EMPTY_MARKER, 5: EMPTY_MARKER, 6: EMPTY_MARKER,
    7: EMPTY_MARKER, 8: EMPTY_MARKER, 9: EMPTY_MARKER
    }
    current_player = ['player', 'computer']

    def update_scores():
        if detect_game_winner(board) == 'Computer':
            scores['computer'] += 1

        if detect_game_winner(board) == 'Player':
            scores['player'] += 1

    def display_scores():
        prompt(f"{'SCOREBOARD'.center(24)}")
        prompt(f"You: {scores['player']} Computer: {scores['computer']}".center(24))

    def check_match_winner():
        if scores['computer'] == WIN_REQ:
            prompt('Computer wins the match!')
            scores['computer'] = 0
            scores['player'] = 0
        if scores['player'] == WIN_REQ:
            prompt('Player wins the match!')
            scores['computer'] = 0
            scores['player'] = 0

    display_welcome()

    while True:
        board = init_board()
        current_player = choose_turn(current_player)

        while True:
            display_board(board)
            choose_square(current_player, board)
            current_player = alternate_player(current_player)
            if check_game_finished(board):
                display_board(board)
                update_scores()
                display_scores()
                check_match_winner()
                break

        if not play_again_check():
            clear_screen()
            prompt("Ok! Thanks for playing Tic Tac Toe!")
            break

play_tic_tac_toe()
