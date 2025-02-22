import random
import os

def clear():
    os.system('clear')

def join_or(lst, delimiter=', ', conjunction='or'):
    str_list = [str(num) for num in lst]

    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return (f'{str_list[0]} {conjunction} {str_list[1]}')

    return (f'{delimiter.join(str_list[:-1])}'
            f'{delimiter}{conjunction} {str_list[-1]}')

def prompt(message, new_line=False):
    if new_line:
        print('\n')
        print(f'--> {message}')
    else:
        print(f'--> {message}')

class Score:
    def __init__(self):
        self.reset()

    def __repr__(self):
        return (f"** Player : {self.scores['player']} |"
                f" Computer : {self.scores['computer']} **")

    def __str__(self):
        return (f"** Player : {self.scores['player']} |"
                f" Computer : {self.scores['computer']} **")

    def display(self):
        prompt(self)

    def update(self, player):
        self.scores[player.name] += 1

    def reset(self):
        self.scores = {'player': 0, 'computer': 0}


class Square:
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER ='O'
    EMPTY_MARKER = ' '

    def __init__(self, marker=' '):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __str__(self):
        return self.marker

    def is_unused(self):
        return self.marker == Square.EMPTY_MARKER

class Board:
    MIDDLE_SQUARE = 5

    def __init__(self):
        self.reset()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def display(self):
        prompt('+---+---+---+', new_line=True)
        prompt(f'| {self.squares[1]} | {self.squares[2]} |'
               f' {self.squares[3]} |')
        prompt('+---+---+---+')
        prompt(f'| {self.squares[4]} | {self.squares[5]} |'
               f' {self.squares[6]} |')
        prompt('+---+---+---+')
        prompt(f'| {self.squares[7]} | {self.squares[8]} |'
               f' {self.squares[9]} |')
        prompt('+---+---+---+')

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return not self.unused_squares()

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def reset(self):
        self.squares = {num: Square() for num in range(1, 10)}

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)
        self.name = 'player'

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)
        self.name = 'computer'

    def move(self, board):
        pass

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    MATCH_GOAL = 3

    def __init__(self):
        self.computer = Computer()
        self.human = Human()
        self.board = Board()
        self.score = Score()
        self.first_player = self.human

    def play_round(self):
        while True:
            if self.first_player == self.human:
                self.board.display()
                self.human_moves()
                if self.game_over():
                    break
                self.computer_moves()
                if self.game_over():
                    break
            else:
                self.computer_moves()
                self.board.display()
                if self.game_over():
                    break
                self.human_moves()
                if self.game_over():
                    break

            clear()

    def play(self):
        self.display_welcome()

        while True:
            self.board.reset()
            self.play_round()
            clear()
            self.board.display()
            self.display_results()
            self.update_score()
            self.score.display()
            self.change_first_player()
            self.next_round()
            clear()
            if self.champ():
                self.display_champ(self.champ())
                self.score.reset()
                if not self.play_again():
                    break
            clear()
        clear()
        self.display_goodbye()

    def human_moves(self):
        valid_choices = self.board.unused_squares()

        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = join_or(choices_list)
            prompt(f"choose a square ({choices_str}): ", new_line=True)
            choice = input()

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            prompt('Sorry, that\'s not a valid choice')

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()

        best_move = self.find_next_move(self.computer)

        if not best_move:
            best_move = self.find_next_move(self.human)

        if Board.MIDDLE_SQUARE in valid_choices:
            best_move = Board.MIDDLE_SQUARE

        if not best_move:
            best_move = random.choice(valid_choices)

        self.board.mark_square_at(best_move, self.computer.marker)


    def find_next_move(self, player):
        valid_choices = self.board.unused_squares()

        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2:
                for key in row:
                    if key in valid_choices:
                        return key

        return None

    def display_welcome(self):
        prompt('Welcome to Tic Tac Toe!')

    def game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def display_results(self):
        if self.is_winner(self.human):
            prompt("You won! Congratulations!", new_line=True)
        elif self.is_winner(self.computer):
            prompt("I won! I won! Take that, human!", new_line=True)
        else:
            prompt("A tie game. How boring.", new_line=True)

    def update_score(self):
        if self.is_winner(self.human):
            self.score.update(self.human)
        if self.is_winner(self.computer):
            self.score.update(self.computer)

    def next_round(self):
        prompt('Press any key to continue...', new_line=True)
        input()

    def is_champ(self):
        return (any(score == TTTGame.MATCH_GOAL
                    for score in self.score.scores.values()))

    def champ(self):
        for player, score in self.score.scores.items():
            if score == TTTGame.MATCH_GOAL:
                return player

        return None

    def display_champ(self, champ):
        prompt(f'{champ.title()} won three games and is the current champ!')

    def play_again(self):
        prompt('Would you like to play again? (y/n)', new_line=True)
        choice = input()

        while not choice or choice[0] not in 'yn':
            clear()
            prompt('Sorry, that\'s an invalid choice. '
                           'Please type (y/n) to continue...\n')
            choice = input()

        return choice == 'y'

    def change_first_player(self):
        if self.first_player == self.human:
            self.first_player = self.computer
        else:
            self.first_player =  self.human

    def display_goodbye(self):
        prompt('Thanks for playing Tic Tac Toe! Goodbye!')

game = TTTGame()
game.play()