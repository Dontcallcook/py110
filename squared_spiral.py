""" 
PROBLEM:
Find the largest sum of consecutive integers in a list.

RULES:
- there may be negative integers

EXAMPLES:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
should be 6: [4, -1, 2, 1]

DATA STRUCTURES:
integer to store highest total

ALGORITHIM:
find the max value in the input list
then loop through the list in twos to find the highest pair using slicing by increasing the indexes each search arr[idx1:idx2 + 1] -> idx1 += 1, idx2 += 1 
if index 2 is greater than the last index in the list:
    - start the loop again
    - increase the value to search for three in a row, 4 in a row and so on
stop looping when index1 is 0 and index2 is len(list) - 1
 """
import pdb
""" def max_sequence(arr):
    highest = max(arr)
    idx1, idx2 = 0, 1
    idx_increase = 1

    # pdb.set_trace()
    while True:
        comparison = sum(arr[idx1:idx2 + 1])
        print(f'comparison split: {arr[idx1:idx2 + 1]}')
        print(f'comparison value: {comparison}')
        print(f'highest value: {highest}')
        if comparison > highest:
            highest = comparison
            print(f'new highest: {highest}')

        if idx1 == 0 and idx2 == len(arr) - 1:
            return highest

        if idx2 > len(arr) - 1:
            idx1 = 0
            idx2 = idx_increase
            idx_increase += 1
        else:
            idx1 += 1
            idx2 += """

def max_sequence(arr):
    if not arr:
        return 0

    highest = current_sub = 0

    for num in arr:
        current_sub = max(num, current_sub + num)
        print(f'current_sub is {current_sub}')
        highest = max(highest, current_sub)
        print(f'highest is {highest}')

    return highest



print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # doesn't account for all negatives in a split
