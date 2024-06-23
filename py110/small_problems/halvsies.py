# PROBLEM:
#     - Take a list and return two lists consisting of the original list cut in half
#     - The First half of the original list should be the first list, and the second half the second list.
#     - If the original list is an odd length, the middle number should be contained in the first list.

# RULES:
#     - If the original list is empty, return two empty lists
#     - If the original list has only one number, return the number in the first list, and then an empty second list

# INPUT:
#     - one list
# OUTPUT:
#     - two nested lists, consiting of the first cut in half

# DATA STRUCTURES:
#     - two nested lists to contain values from original list

# ALGORITHM:
#     - Initiate list to contain two new lists -> holding_list = []
#     - check if original list is odd or even
#     - Slice the original list down the middle
#         -if even:
#             - first_half = original_list[:len(original_list) // 2]
#             - second_half = original_list[len(original_list // 2:]
#         -if odd:
#             - first_half = original_list[:(len(original_list) // 2) + 1]
#             - second_half = original_list[(len(original_list // 2) + 1:]
#     - Append first half to holding_list
#     - Append second half to holding_list

def halvsies(lst):
    if len(lst) % 2 == 0:
        return [lst[:len(lst) // 2], lst[len(lst) // 2:]]
    
    if len(lst) % 2 == 1:
        return [lst[:len(lst) // 2 + 1], lst[len(lst) // 2 + 1:]]
        
    
    

# TEST CASES:
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
