import random

# PROBLEM:
#     Write a function that takes no arguments are returns a UUID as a string
    
#     Rules:
#         returns a pattern of 8-4-4-4-12 characters.
#         the characters are random hexidecimal characters: 0-9 a-f

# Input:
#     no input

# Output:
#     string

#ALGORITHM:
#     initialize list of hexidecimal chacaters: 0-9, a-f
#     intialize hex_value consisting of strings -> ["xxxxxxxx", "xxxx", "xxxx", "xxxx", "xxxxxxxxxxxx"]
#     loop through list and sublists
#     for each value replace with random.randomchoice(hex_list)
#     return joined list -> '-'.join(hex_value)

hex_list = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hex_template = [8, 4, 4, 4, 12]

def uuid_maker():
    hex_number = []
    
    for section in hex_template:
        hex_number.append([random.choice(hex_list) for _ in range(section)])
    
    hex_number = '-'.join(sublist_joiner(hex_number))
    
    return hex_number

def sublist_joiner(lst):
    return [''.join(sublist) for sublist in lst]

print(uuid_maker())