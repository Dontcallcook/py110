# PROBLEM: 
# Must build a valid structure from number of blocks provided. A valid structure has certain rules:
    
# RULES:
#     Explicit Rules:
#         - Blocks are of equal length and width
#         - The structure is made of layers
#         - The top layer is one block
#         - A block must be supported by 4 blocks underneath it
#         - A block in a lower layer can support more than one block ontop of it
#         - There can be no gaps between blocks
    
#     Implicit Rules:
#         - The top layer must have one block
#         - Each layer must have at least 4 blocks before the next layer starts
#         - The number of cubes in a layer is proportional to the layer number:
#             - From top to bottom - cube amount is equal to layer number * layer number
#               -> layer 1 * layer 1 == 1
#               -> layer 2 * layer 2 == 4
#               -> layer 3 * layer 3 == 9
#         - It's ok to have 0 remaining blocks

# INPUTS:
#     - Is the number of blocks input a string or an integer?

# OUTPUTS:
#     - integer for the number of blocks leftover after building tallest structure

# EXAMPLES:
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

# DATA STRUCTURES:
#    - list that tracks the number of blocks in the valid structure.
#    - [1, 4, 9, 16] -> each integer represents the amount of cubes in a layer

# ALGORITHM:
# From the input_blocks provided build a valid structure.
#         - 1. Initialise an empty list
#         - 2. Intialise variable -> layer_number = 1
#         - 3. Initialise variable -> remaining blocks = input_blocks
#         - 4. Calculate needed blocks for new layer
#                   needed blocks = layer_number ** 2
#         - 5. Check if remaining blocks is >= needed_blocks    
#         - 6. If remaining blocks is >= needed blocks, add needed_blocks to list
#         - 7. increase layer_number by 1
#.        - 8. needed_blocks = layer_number ** 2
#.        - 9. remaining_blocks -= last_element of list

def calculate_leftover_blocks(input_blocks):
    structure_list = []
    remaining_blocks = input_blocks
    layer_number = 1
    
    while remaining_blocks >= layer_number ** 2:
        structure_list.append(layer_number ** 2)
        layer_number += 1
        remaining_blocks -= structure_list[-1]
    
    return remaining_blocks
    
    
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(50))