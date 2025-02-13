import os
import random

LINE_SPACE = '\n'

def prompt(message):
    print(f'-->> {message}')

class Score:
    def __init__(self, human, computer):
        self.reset(human, computer)

    def __str__(self):
        return (f'* * {self._player1}: {self.score[self._player1]} -- '
                f'{self._player2}: {self.score[self._player2]} * *')

    def display(self):
        print(LINE_SPACE)
        print('Scoreboard:'.center(32))
        print(self)
        print(LINE_SPACE)

    def update(self, winner):
        self.score[winner] += 1

    def get_champ(self):
        for player, score in self.score.items():
            if score == 5:
                return player

        return None

    def reset(self, human, computer):
        self._player1 = human
        self._player2 = computer
        self.score = {human: 0, computer: 0}

class Player:
    def __init__(self):
        self.move = None
        self.move_history = []

    def __repr__(self):
        return 'Player'

    def __str__(self):
        return 'Player'

    def display_move_history(self):
        prompt(f"{self}'s past moves: "
               f"{', '.join(str(move) for move in self.move_history)}")

class DefaultComputer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Computer'

    def __str__(self):
        return 'Computer'

    def choose(self):
        self.move = Move(random.choice(Move.CHOICES))
        self.move_history.append(self.move)

class Hal(Player):
    def __init__(self):
        super().__init__()
        self._moves = Move.CHOICES + ['scissors', 'scissors', 'scissors']

    def __repr__(self):
        return 'Hal'

    def __str__(self):
        return 'Hal'

    def choose(self):
        self.move = Move(random.choice(self._moves))
        self.move_history.append(self.move)

class R2d2(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'R2D2'

    def __str__(self):
        return 'R2D2'

    def choose(self):
        self.move = Move('rock')
        self.move_history.append(self.move)

class Daneel(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Daneel'

    def __str__(self):
        return 'Daneel'

    def choose(self, human):
        if not self.move_history:
            self.move = Move(random.choice(Move.CHOICES))
        else:
            self.move = human.move_history[-1]
        self.move_history.append(self.move)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt('Make your move!\nrock, paper, scissors, lizard, or Spock: ')

        while True:
            choice = input().lower()
            if choice.lower() in Move.CHOICES:
                break

            prompt(f'Sorry, {choice} is not valid')

        self.move = Move(choice)
        self.move_history.append(self.move)

class Move:
    CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    OUTCOMES = {
    'rock': {
        'scissors': 'rock CRUSHES scissors',
        'lizard': 'rock CRUSHES lizard'
    },
    'paper': {
        'rock': 'paper COVERS rock',
        'spock': 'paper DISPROVES Spock'
    },
    'scissors': {
        'paper': 'scissors CUTS paper',
        'lizard': 'scissors DECAPITATES lizard'
    },
    'lizard': {
        'paper': 'lizard EATS paper',
        'spock': 'lizard POISONS Spock'
    },
    'spock': {'rock': 'Spock VAPORISES rock',
              'scissors': 'Spock SMASHES scissors'
    },
    }

    def __init__(self, choice):
        self.choice = choice

    def __str__(self):
        return f'{self.choice}'

    def __repr__(self):
        return f'{self.choice}'

    @staticmethod
    def compare(human, computer):
        if computer.move.choice in Move.OUTCOMES[human.move.choice]:
            return human
        if human.move.choice in Move.OUTCOMES[computer.move.choice]:
            return computer

        return None

class RPSGame:
    OPPONENTS = {'1': DefaultComputer, '2': R2d2, '3': Daneel, '4': Hal}

    def __init__(self):
        self._human = Human()
        self._computer = DefaultComputer()
        self._score = Score(self._human, self._computer)

    @staticmethod
    def _clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def _display_welcome_message(self):
        prompt('Welcome to Rock Paper Scissors Lizard Spock!')
        print(LINE_SPACE)

    def _display_opponents(self):
        prompt('Choose your opponent: (1-4)\n'
               '1. Standard | 2. R2D2 | 3. Daneel | 4. Hal\n')

    def _opponent_selection(self):
        self._display_opponents()
        opponent = input()

        while opponent not in RPSGame.OPPONENTS:
            self._clear()
            prompt('Choice invalid: Please pick a number from 1-4')
            print(LINE_SPACE)
            self._display_opponents()
            opponent = input()

        return RPSGame.OPPONENTS[opponent]()

    def _display_goodbye_message(self):
        prompt('Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def _get_result(self):
        winner = Move.compare(self._human, self._computer)
        if winner == self._human:
            return self._human, self._computer
        if winner == self._computer:
            return self._computer, self._human

        return None, None

    def _display_result(self, winner, loser):
        prompt(f'{self._human} chose: {self._human.move}')
        prompt(f'{self._computer} chose: {self._computer.move}')

        if winner:
            prompt('!!>>'
                   f'{Move.OUTCOMES[winner.move.choice][loser.move.choice]}'
                   '<<!!')
            print(LINE_SPACE)

            if winner == self._human:
                prompt('You win!')
            if winner == self._computer:
                prompt('Computer wins!')
        else:
            prompt("It's a tie!")

    @staticmethod
    def _display_next_round():
        print(LINE_SPACE)
        input('Press any key to continue to the next round...')

    def play(self):
        self._clear()
        self._display_welcome_message()
        opponent = self._opponent_selection()
        self._computer = opponent
        self._score = Score(self._human, self._computer)
        self._clear()
        while True:
            if isinstance(self._computer, Daneel):
                self._computer.choose(self._human)
            else:
                self._computer.choose()
            self._human.choose()
            winner, loser = self._get_result()
            self._clear()
            self._display_result(winner, loser)
            if winner:
                self._score.update(winner)
            self._score.display()
            print('Move history:')
            self._human.display_move_history()
            self._computer.display_move_history()
            champ = self._score.get_champ()
            if champ:
                self._display_champ(champ)
                self._score.reset(self._human, self._computer)
                if not self._play_again():
                    break
            self._display_next_round()
            self._clear()
        self._clear()
        self._display_goodbye_message()

    def _display_champ(self, champ):
        print(LINE_SPACE)
        prompt(f'{champ} was the first to win 5 games and is the new champ!')

    def _play_again(self):
        prompt('Would you like to play again? (y/n) ')
        answer = input()
        print(LINE_SPACE)

        while answer.lower() not in 'yn':
            self._clear()
            prompt("Sorry, your choice is invalid!\n"
                   "Type 'y' to play again or 'n' to quit: ")
            answer = input()

        return answer.lower().startswith('y')

RPSGame().play()