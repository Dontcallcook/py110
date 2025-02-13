"""
PROBLEM:
return the minimum sum of 5 consecutive integers in a list

EXAMPLE:
[1, 2, 3, 4, 5, 6] ==> 15

DATA STRUCTURE:
int to store current lowest sum

ALGORITHM:
use two indexes to create window of 5 values in list
find sum of window
keep moving window along list until the last index is equal to the end of the list
"""
def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    smallest = float('inf')

    for i in range(len(lst) - 4):
        current_sum = sum(lst[i:i + 5])
        if current_sum < smallest:
            smallest = current_sum
    
    return smallest

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)