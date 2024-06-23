# All of these examples should print True
"""
ALGORITHIM:
    1. intitalise start (1), end(len(sequence)), and middle -> (end - start) // 2 + start
    1. find middle list item -->
        - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        -  0  1  2  3  4  5  6  7  8, 9
        - (end - start) // 2 + start
        - (10  -   0  ) // 2 + 0 = 5
        - 10   -   5  ) // 2 + 5 = 

    2. check if middle list item is search item
        3. if it is the search item, return middle item
        4. if not:
            - check if middle item is greater or lesser than search item
            - if middle item is greater, discard second half of list
                - set end index to the position of middle item
            - if middle item is lesser, discard first half of list
                - set start index to the position of middle item + 1
    5. repeat steps 1-4 with half of list

"""

import pdb

# def binary_search(data, item, start=1):
#     # pdb.set_trace()
#     end = len(data)
    
#     while True:
#         middle = (start + end) // 2
#         if data[middle] == item:
#             return middle
#         elif len(data[start:end]) == 1:
#             return -1
#         else:
#             if data[middle] > item:
#                 end = middle
#             else:
#                 start = middle

def binary_search(data, item, start=0, end=None):
    if end == None:
        end = len(data)
    
    middle = (start + end) // 2

    if len(data[start:end]) <= 1:
        if data[middle] == item:
            return middle
        else:
            return -1

    if data[middle] == item:
        return middle
    else:
        if data[middle] > item:
            return binary_search(data, item, start=start, end=middle)
        else:
            return binary_search(data, item, start=middle, end=end)




businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6) 
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)