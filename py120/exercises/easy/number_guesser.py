import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self._guesses = int(math.log2(high - low + 1)) + 1
        self._guess_range = range(low, high + 1)
        self._answer = random.choice(self._guess_range)

    def play(self):
        while self._guesses > 0:    
            self.display_remaining_guesses()
            guess = self.get_guess()
            self._guesses -= 1
            result = self.resolve_guess(guess)
            if result == 'high':
                print("Your guess is too high.")
            elif result == 'low':
                print("Your guess is too low.")
            else:
                print("""That's the number! \n\nYou won!""")
                break
        if self._guesses <= 0:
            print("You have no more guesses. You lost!")

    def resolve_guess(self, guess):
        if guess > self._answer:
            return 'high'
        elif guess < self._answer:
            return 'low'
        else:
            return 'win'

    def display_remaining_guesses(self):
        print(f'You have {self._guesses} guesses remaining.')

    def get_guess(self):
        guess = input(f'Enter a number between {self.low} and {self.high}: ')
        while not self.valid_guess(guess):
            guess = input(f"Invalid guess. Enter a number between "
                          f"{self.low} and {self.high}: ")

        return int(guess)
        
    def valid_guess(self, guess):
            try:
                guess = int(guess)
                if guess not in self._guess_range:
                    return False
            except ValueError:
                return False
            else:
                return True

game = GuessingGame(501, 1500)
game.play()