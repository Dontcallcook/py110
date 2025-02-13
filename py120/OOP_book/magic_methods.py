# class Car:

#     def __init__(self, id, year, color):
#         self._id = id
#         self._year = year
#         self.color = color
    
#     def __str__(self):
#         return f'{self.color.title()} {self._year} {self._id}'

#     def __repr__(self):
#         return f'Car({repr(self._id)} {self._year} {repr(self.color)})'

#     @property
#     def color(self):
#         return f'{self._color}'
    
#     @color.setter
#     def color(self, new_color):
#         self._color = new_color


# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')


# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     # __iadd__ method omitted; we don't need it for this exercise

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'
    
#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)
    
#     def __mul__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         new_x = self.x * other.x
#         new_y = self.y * other.y
#         return new_x + new_y

#     def __abs__(self):
#         sum_squares = (self.x ** 2) + (self.y ** 2)
#         return sum_squares ** 0.5

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)

# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# class Candidate:

#     def __init__(self, name):
#         self._name = name
#         self._votes = 0

#     def __iadd__(self, other):  
#         self._votes += other
#         return self


# class Election:

#     def __init__(self, candidates):
#         self._candidates = candidates
    
#     def results(self):
#         most_votes = 0
#         vote_count = 0
#         winner = None

#         for candidate in candidates:
#             vote_count += candidate._votes
#             if candidate._votes > most_votes:
#                 most_votes = candidate._votes
#                 winner = candidate._name
        
#         for candidate in candidates:
#             name = candidate._name
#             votes = candidate._votes
#             print(f'{name}: {votes}')

#         print(f'Winner: {winner}')
        
    
# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()