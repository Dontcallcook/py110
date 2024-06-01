# PROBLEM:
#     write a function that takes a list and reverses the list in place - it mutates the list.

# DATA STRUCTURES:
#     list

# INPUT:
#     list

# OUTPUT:
#     mutated list

# ALGORITHM:
#     1. inititiate two indexes for start [0] and end[-1] of list
#         - [1, 2, 3, 4, 5] or [1, 2, 3, 4]
#         -  0  1  2  3  4      0  1  2  3
#     2. swap list[start_index] with list[end_index]
#     3. increase start_index by one
#     4. decrease end_index by one
#     5. repeat steps 2-4 until start_index == len(lst) // 2



def reverse_list(lst):
    start_idx = 0
    end_idx = len(lst) - 1
    
    while start_idx != len(lst) // 2:
        lst[start_idx], lst[end_idx] = lst[end_idx], lst[start_idx]
        start_idx += 1
        end_idx -= 1
    
    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result)  # prints [4, 3, 2, 1]
print(list1 is result)  # prints True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2)  # prints ['e', 'd', 'c', 'b', 'a']
print(list2 is result2)  # prints True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3)  # prints ['abc']
print(list3 is result3)  # prints True

list4 = []
result4 = reverse_list(list4)
print(result4)  # prints []
print(list4 is result4)  # prints True