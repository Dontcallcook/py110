list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]


# def interleave(list1, list2):
#     idx = 0
#     new_list = []
#     while idx < len(list1):
#         new_list.extend([list1[idx], list2[idx]])
#         idx += 1
#     return new_list
        
def interleave(list1, list2):
    return [element for list_tuple in zip(list1, list2) for element in list_tuple]


print(interleave(list1, list2) == expected)      # True