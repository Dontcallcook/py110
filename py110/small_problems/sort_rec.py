"""
EXAMPLE:

[9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# repeat until each sub-list contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

"""
import pdb

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    else:
        nest1 = merge_sort(lst[:len(lst)//2])
        nest2 = merge_sort(lst[len(lst)//2:])
    
    return merge(nest1, nest2)

def merge(list1, list2):
    pdb.set_trace()
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#               'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#               'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#               43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#               35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)