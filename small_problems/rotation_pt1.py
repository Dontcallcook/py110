# PROBLEM:
# Write a function that rotates a list by moving the first element to the end of the list.
# Do not modify the original list.

# RULES:
# Explicit:
# - List can't be modified
# - If the input is empty, return an empty list

# Implicit:
# - The list output she be a new list to which we assign values
# - If input is not a list, return None

# INPUT:
# List of values

# OUPUT:
# New list with first element of the original list moved to last index position

# EXAMPLES:
# [7, 3, 5, 2, 9, 1] -> [3, 5, 2, 9, 1, 7]
# ['a', 'b', 'c'] -> ['b', 'c', 'a']
# ['a'] -> ['a']
# [1, 'a', 3, 'c'] -> ['a', 3, 'c', 1]
# [{'a': 2}, [1, 2], 3] -> [[1, 2], 3, {'a': 2}]
# [] -> []
# None -> None
# 1 -> None

# DATA STRUCTURES:
# List input
# New list consisiting of input list with first value in last index position

# ALGORITHM:
# 1. Assign new list as input list
# 2. capture value from first index position of new list
# 3. remove value from first index position
# 4. append the value to the end of the list

def rotate_list(data):
    if not data:
        return data
    
    if not isinstance(data, list):
        return None
        
    return data[1:] + [data[0]]
    
print(rotate_list([7, 3, 5, 2, 9, 1]))           # [3, 5, 2, 9, 1, 7]
print(rotate_list(['a', 'b', 'c']))              # ['b', 'c', 'a']
print(rotate_list(['a']))                        # ['a']
print(rotate_list([1, 'a', 3, 'c']))             # ['a', 3, 'c', 1]
print(rotate_list([{'a': 2}, [1, 2], 3]))       # [[1, 2], 3, {'a': 2}]
print(rotate_list([]))                           # []

    