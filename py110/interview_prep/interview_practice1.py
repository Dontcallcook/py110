"""
PROBLEM:
return a list that is the amount of numbers that are smaller than the number of the input list

EXAMPLE:
[3, 2, 2, 1] ==> [2, 1, 1, 0]

DATA STRUCTURE:
list to store count
set to store seen numbers

ALGORITHM:
loop through each element of list
init count as 0

    for each element check the other elements in the list
        check if element in seen
        if not in seen
            if number less than the checked number
                increase count by 1
        add the current number to seen
    add count to output_list


"""
import pdb

def smaller_numbers_than_current(lst):
    output_list = []
    
    for i in range(len(lst)):
        count = 0
        seen = set()
        for j in range(len(lst)):
            if lst[j] not in seen:
                if lst[j] < lst[i]:
                    count += 1
            seen.add(lst[j])
        output_list.append(count)

    return output_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)