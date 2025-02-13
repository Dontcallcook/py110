# Generate a multiplication table.
# Example: The table should look like this for size = 3:
# [[1, 2, 3], 
#  [2, 4, 6], 
#  [3, 6, 9]]
"""
PROBLEM:
generate a multiplication table consisting of a list of nested lists
each nested list should be one set of multiples -> [1, 2, 3] -- [2, 4, 6] -- [3, 6, 9] etc.

the number of nests is the input integer
the number of numbers in a nest is the input integer

EXAMPLE:
2 -> [[1, 2], [2, 4]]
3 -> [[1, 2, 3], [2, 4, 6],[3, 6, 9]]

DATA STRUCTURE:
a list to store nested lists of multiplications (comprehension?)
ranges to create multiplications

ALGORITHM:
create nested comprehsion consisting of empty lists
the number of empty lists should be the input integer E.G:
3 -> [[], [], []]

loop through empty lists
use a range and multiple to store correct numbers
multiple should increases each time a nest is filled
a nest is filled when the length of it is the same as the input integer

when the final nest is filled, return the table
"""
# i = 0
# num = 1
# num = 2
# num = 3

# i = 1
# num = 2
# num = 3

def multiplication_table(size):
    table = [[j * (i + 1) for j in range(1, size + 1)] for i in range(size)]

    return table

print(multiplication_table(3))  

# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# the multiple is == to nest index + 1 -> 1, 2, 3