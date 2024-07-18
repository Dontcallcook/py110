
"""
PROBLEM:
Write a function that filters letters through a funnel and return the string in the correct order.
The letters drop out of the funnel from smallest to largest, e.g., 'a' is smaller than 'b' which is smaller than 'c' etc.
The characters are standard upper and lower case letters.

The layers of the funnel increase by one each time:
    The first layer is one letter
    The second layer is two letters
    The third layer is three letters
    and so on...

INPUT:
A nested list representing the funnel. Each nest is longer than the last by 1.
The first item is at the end of the nested list -> {[["a","e","c","f"],["d","i","h"],["j","g"],["b"] <--- ] list1[-1][0]

OUTPUT:
A string in the correct order -> 'dfegh'

ALGORITHIM:
1. loop through nests
2. add the character in the bottom funnel list to the string
3. check for the smallest value in the remaining nests
4. check if that value is able to move to the list below:
    - it is able to move below if the last below contains the value None
    - and if the index of None is equal to the index of the moved int or 1 more than the moved int
5. if the value can move, move it and replace that value wiht None, if it can't move check the next smallest value

check which value is smaller and able to move into the second to last nest
move value into second to last nest

repeat for all lists
TEST_CASES:
funnel_out([["q"]]),"q")
funnel_out([["b","c"],["a"]]),"abc")
funnel_out([["d","a","c"],["b","e"],["f"]]),"fbadec")
funnel_out([["a","e","c","f"],["d","i","h"],["j","g"],["b"]]),"bghcfiejda")

PROBLEM:
check if a value is able to fall into a lower list
a value can fall into a lower list if it is in the right position and smaller than others taht are also in the right posiiton:
    It is in the right position if there is a space in a lower list:
        a higher letter can replace a lower space if the index is the same or + 1
        [[]]
"""



import pdb
def funnel_out(funnel):
    output_string = ''
    funnel = list(reversed(funnel))

    for i, row in enumerate(funnel):
        if len(row) == 1: #add bottom row character to string 
            output_string += row[0]
            row[0] = None
        
        if i == len(funnel) - 1:
            return output_string

        if None in row: #check if empty spaces
            empty_idx = row.index(None) # find the empty space index
            print(f'empty_idx is {empty_idx}')
            
            upper_row_min_value = min(funnel[i + 1])
            upper_row_min_value_idx = funnel[i + 1].index(min(funnel[i + 1]))

            print(upper_row_min_value)
            print(upper_row_min_value_idx)

            if upper_row_min_value_idx <= empty_idx + 1:
                row[empty_idx] = upper_row_min_value
                funnel[i + 1][upper_row_min_value_idx] = None

    
print(funnel_out([["a","e","c","f"],["d","i","h"],["j","g"],["b"]]))

