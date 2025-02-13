
"""
PROBLEM:
Find the most efficient move for a player to make given a list of moves, and move choices (represented by nested lists)

"""

def unique_sequence(lst):
    output_list = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] != output_list[-1]:
            output_list.append(lst[i])

    return output_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 2]
expected = [1, 2, 6, 5, 3, 4, 2]
print(unique_sequence(original) == expected)      # True