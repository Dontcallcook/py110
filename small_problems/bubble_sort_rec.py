import pdb
"""
AGLORITHIM:
    - loop through list using indexing to select two values
    - check if first and second value need swapping
    - if they need swapping:
        - swap
        - increase indexes
        - set swaps_made to True
    - else
        - increase the indexes
    - when the end of the list is reached, check if any swaps have occurred
        - if they have occurred:
            - set the swaps_made variable to False
            - loop through list again
        - else:
            - return the list
"""
def bubble_sort(data, idx1=0, idx2=1, swaps_made=True, passes=0):
    # pdb.set_trace()
    print(f'Swaps_made is {swaps_made}')
    if idx1 == len(data) - 1:
        if not swaps_made: # overall sort base case
            return data
        else:
            return bubble_sort(data, idx1=0, idx2=1, False, passes + 1)
    
    if data[idx1] > data[idx2]:
        data[idx1], data[idx2] = data[idx2], data[idx1]
        return bubble_sort(data, idx1 + 1, idx2 + 1, True)
    
    else:
        return bubble_sort(data, idx1 + 1, idx2 + 1)

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1)# == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2)# == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3) == expected)                 # True