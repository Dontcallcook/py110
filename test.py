# accounts = {
#     'HSBC': {2024: {month: None for month in range(1, 13)}}, 
#     'Coinbase': {2024: {month: None for month in range(1, 13)}}, 
#     'Trading212': {2024: {month: None for month in range(1, 13)}}, 
#     'Chip': {2024: {month: None for month in range(1, 13)}}, 
#     'Oxbury': {2024: {month: None for month in range(1, 13)}}, 
#     'Monument': {2024: {month: None for month in range(1, 13)}},
# }

# def not_valid_number(string):
#     try:
#         int(string)
#     except ValueError:
#         return True
#     else:
#         return False

# def get_balance(account):
#     for q in ['year', 'month', 'balance']:
#         if q == 'year':
#             year = input(f'What\'s the current {q}? ')
#             while not_valid_number(year):
#                 print("That doesn't seem to be a valid number...")
#                 year = input(f'What\'s the current {q}? ')
#         elif q == 'month':
#             month = input(f'What\'s the current {q}? ')
#             while not_valid_number(month):
#                 print("That doesn't seem to be a valid number...")
#                 month = input(f'What\'s the current {q}? ')
#         else:
#             balance = input(f'How much do you have in {account}? ')
#             while not_valid_number(balance):
#                 print("That doesn't seem to be a valid number...")
#                 balance = input(f'What\'s the current {q}? ')

# def store_balance(account, balance):
#     latest_year = accounts[account][list(accounts[account].keys())[-1]]
#     latest_month = latest_year[list(latest_year.keys())[-1]]
#     print(latest_year)
#     print(latest_month)
#     accounts[account][latest_year][latest_month] = balance

# for account in accounts:
#     get_balance(account)

# 1. Write a function that takes a list of integers and returns a new list with only the prime numbers. Use a list comprehension in your solution.

# All of these examples should print True

"""
PROBLEM:
return a list of values from a matrix in spiral order
the matrix can be any size
spiral order means the direction follows this pattern:
each index of first row
last index of each row
each index of last row in reverse
first index of each row except first in reverse

ALGORITHM:
init empty output_list

loop through row

"""
# import pdb

# def spiral_traversal(matrix):
#     output_list = []
#     center = {'x': len(matrix) // 2, 'y': len(matrix[0]) // 2}.values()
    
#     right_target = len(matrix[0])
#     left_target = -len(matrix[0]) - 1
#     down_target = len(matrix)
#     up_target = -len(matrix)

#     current_coord = {'x': 0, 'y': 0}
#     current_direction = 'right'
#     # pdb.set_trace()
#     while current_coord != center:
#         print(f'current direction is {current_direction}')
        
#         if current_direction == 'right':
#             while current_coord['x'] != right_target:
#                 output_list.append(matrix[current_coord['y']][current_coord['x']])
#                 current_coord['x'] += 1
#             right_target -= 1
#             current_direction = 'down'
#             current_coord['x'] -=1
#             print(f'current coordinates are {current_coord}')
#             print(f'output_list is {output_list}')

        
#         elif current_direction == 'down':
#             current_coord['y'] += 1
#             while current_coord['y'] != down_target:
#                 output_list.append(matrix[current_coord['y']][current_coord['x']])
#                 current_coord['y'] += 1
#             down_target -= 1
#             current_direction = 'left'
#             current_coord['y'] -=1
#             print(f'current coordinates are {current_coord}')
#             print(f'output_list is {output_list}')
        
#         elif current_direction == 'left':
#             current_coord['x'] -= 1
#             while current_coord['x'] != left_target:
#                 print(f'left target is {left_target}')
#                 output_list.append(matrix[current_coord['y']][current_coord['x']])
#                 current_coord['x'] -= 1
#             left_target += 1
#             current_direction = 'up'
#             current_coord['x'] +=1
#             print(f'current coordinates are {current_coord}')
#             print(f'output_list is {output_list}')
        
#         elif current_direction == 'up':
#             current_coord['y'] -= 1
#             while current_coord['y'] != up_target:
#                 output_list.append(matrix[current_coord['y']][current_coord['x']])
#                 current_coord['y'] -= 1
#             up_target += 1
#             current_direction = 'right'
#             current_coord['y'] +=1
#             print(f'current coordinates are {current_coord}')
#             print(f'output_list is {output_list}')

#     return output_list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(spiral_traversal(matrix))
# # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# current_coord = {'x': 0, 'y': 0}
# print(matrix[2][-3])

# def group_anagrams(lst):
#     anagram_set = set()

#     for word in lst:
#         anagram_set.add(''.join(sorted(word)))

#     anagrams = {anagram: [] for anagram in anagram_set}

#     for word in lst:
#         anagrams[''.join(sorted(word))].append(word)
    
#     return list(anagrams.values())

"""
PROBLEM:
find the number of anagrams in a list of words

EXAMPLES:
['aet', 'tea', ban', 'nab', 'nam']

DATA STRUCTURES:
sorted word set to eliminate duplicate anagrams:
input ==> ['aet', 'tea', ban', 'nab', 'nam']
output --> {'aet', abn', 'amn'}

ALGORITHM:
sort the words so they are the same alphabetically
put them in a set to remove duplicates
return the length of the set
"""

lst = [1, 2, 3, 4, 5, 6]

target_letters = ['a', 'b', 'b', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

my_dict = {char: {'present': False, 'count': 0} for char in target_letters}

for char in characters:
    if char in my_dict:
        my_dict[char]['present'] = True
        my_dict[char]['count'] = my_dict[char].get('count', 0) + 1

print(my_dict)