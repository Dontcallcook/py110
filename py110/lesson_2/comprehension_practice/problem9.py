lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# ALGORITHM:
#     intialize empty list
#     loop through dictionaries and check values:
#           for each dictionary, combine all values into one list
#           check if all values are even numbers
#           if all values are even numbers, append dictionary to new list
#     

# def only_evens(subdict):
#     evens_list = []
    
#     for dictionary in lst:
#         for key, sublist in dictionary.items():
#             if all(value % 2 == 0 for value in dictionary.values()):
#                     evens_list.append({key: sublist})
#     return evens_list
                    
# print(only_evens(lst))

def evens_check(num_list):
    return all(num % 2 == 0 for num in num_list)

def filter_evens(data):
    evens = []
    combined_list = []
    
    for dictionary in data:
        for num_list in dictionary.values():
            combined_list += [num for num in num_list]
        
        if evens_check(combined_list):
            evens.append(dictionary)
        combined_list = []
    
    return evens

print(filter_evens(lst))
    