# Question 1
# All objects
# True
# print('hello'.__class__)
# print([1, 2, 3, 'happy days'].__class__)
# print((142).__class__)
# print({1, 2, 3}.__class__)
# print(1.2345.__class__)


# Question 2
# class AngryCat:
#     def hiss(self):
#         print('Hisssss!!!')

# cat1 = AngryCat()


# Question 3
# class SpeedMixin:
#     def go_fast(self):
#         print(f'I am a super fast {self.__class__.__name__}')

# class Car(SpeedMixin):
#     def go_slow(self):
#         print('I am safe and driving slow.')

# class Truck(SpeedMixin):
#     def go_very_slow(self):
#         print('I am a heavy truck and like going very slow.')

# car1 = Car()
# car1.go_fast()


# Question 4
# .__class__.__name__


# Question 5
# print(vars(Fruit('orange')))     # {}
# print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}


# Question 10

# class Cat:
#     _cats_count = 0

#     def __init__(self, type):
#         self.type = type
#         self.__class__._cats_count += 1

#     @classmethod
#     def cats_count(cls):
#         return cls._cats_count

# print(Cat._cats_count)
# cat1 = Cat('Tabby')
# print(cat1.__class__._cats_count)



# EASY 2

# Question 1
# Question 2

# class Game:
#     count = 0

#     def __init__(self, game_name):
#         self.game_name = game_name
#         Game.count += 1

#     def play(self):
#         return f'Start the {self.game_name} game!'

# class Bingo(Game):
#     def __init__(self, game_name, player):
#         super().__init__(game_name)
#         self.player_name = player

# class Scrabble(Game):
#     def __init__(self, game_name, player1, player2):
#         super().__init__(game_name)
#         self.player_name1 = player1
#         self.player_name2 = player2

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

# Question 5

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

Hello.hi()


# Question 6
class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>