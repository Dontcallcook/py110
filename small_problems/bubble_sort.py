"""
PROBLEM: 
    Write a program that sorts a list by comparing adjacent values: 
        - [1, 2, 3, 4, 5] -> first check [1, 2] then check [2, 3] then check [3, 2]

INPUT: 
    list containing unsorted values 

OUTPUT: 
    mutated list containing sorted values 

DATA STRUCTURE: 
    list 

ALGORITHIM:
    Use a while loop to loop through values of list until no swaps made
        - initiate variable swaps_made = False
    check if swap necessary:
        - isolate first two values in list using indexing
        - if first value is greater than second value:
            - swap values, swaps_made = True, increase both indexes by 1
        - else:
            - increase both indexes by 1
        
"""

def bubble_sort(data, swaps_made=True):
    while swaps_made:
        swaps_made = False
        idx = 1

        for i, num in enumerate(data):
            if data[i] == data[-1]:
                break
            elif data[i] > data[idx]:
                data[i], data[idx] = data[idx], data[i]
                idx += 1
                swaps_made = True
            else:
                idx += 1

    return data



# TEST CASES:
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True