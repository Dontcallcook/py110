#PROBLEM:
 #   - write a program that counts the number of elements in a list and returns a string of the item and the number of times it occurs: 'car => 4'

#DATA STRUCTURES:
 #   - use a dictionary to store items as keys and count as values
  #  - allows us to check if an item has already been counted using dictionary.get(item)

#ALGORITHM:
 #   - loop through vehicles
  #  - check if item is already in the dictionary
   # - if not in the dictionary, add item to dictionary as a key and the value as a count

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']


def count_occurrences(lst):
    item_dict = {}
    for item in lst:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    
    for item, count in item_dict.items():
        print(f'{item} => {count}')

count_occurrences(vehicles)