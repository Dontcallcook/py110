"""
class: Score

Responsibilities:
 - initiates an empty scoreboard
 - updates and keeps track of score
 - displays score

 Collaborators:
 - Human
 - Computer
"""

import random

class Score:
    def __init__(self, human, computer):
        self._human = human
        self._computer = computer
        self.score = {self._human: 0, self._computer: 0}

    def __str__(self):
        return f'<< * * {self._human}: {self.score[self._human]}, {self._computer}: {self.score[self._computer]} * * >>'

    def display(self):
        print(self)

    def update(self, winner):
        self.score[winner] += 1

    def get_champ(self):
        for player, score in self.score.items():
            if score == 5:
                return player

        return None

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

    def __repr__(self):
        return 'Player'

    def __str__(self):
        return 'Player'

class Computer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Computer'

    def __str__(self):
        return 'Computer'

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = Score(self._human, self._computer)

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _get_winner(self):
        if self._human_wins():
            return self._human
        elif self._computer_wins():
            return self._computer
        else:
            return None

    def _display_winner(self, winner):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if winner == self._human:
            print('You win!')
        elif winner == self._computer:
            print('Computer wins!')
        else:
            print("It's a tie")

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            winner = self._get_winner()
            self._display_winner(winner)
            if winner:
                self._score.update(winner)
            self._score.display()
            champ = self._score.get_champ()
            if champ:
                self._display_champ(champ)
                if not self._play_again():
                    break

        self._display_goodbye_message()

    def _display_champ(self, champ):
        print(f'{champ} was the first to win 5 games and is the new champ!')

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

RPSGame().play()