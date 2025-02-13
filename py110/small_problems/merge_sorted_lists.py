import pdb

def merge(lst1, lst2):
    sorted_list = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            sorted_list.append(lst1[i])
            i += 1
        else:
            sorted_list.append(lst2[j])
            j += 1

    if i < len(lst1):
        sorted_list.extend(lst1[i:])
    else:
        sorted_list.extend(lst2[j:])
    
    return sorted_list

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    first_half = merge_sort(lst[:len(lst) // 2])
    second_half = merge_sort(lst[len(lst) // 2:])

    return merge(first_half, second_half)

print(merge([2, 6, 7, 9], [0, 1, 5, 8]))
# i is 0 AND j is 0 ==> [0]
# i is 0 AND j is 1 ==> [0, 1]
# i is 0 AND j is 2 ==> [0, 1, 2]
# i is 1 AND j is 2 ==> [0, 1, 2, 5]
# i is 1 AND j is 3 ==> [0, 1, 2, 5, 6]
# i is 2 AND j is 3 ==> [0, 1, 2, 5, 6, 7]
# i is 3 AND j is 3 ==> [0, 1, 2, 5, 6, 7]
# i is 3 AND j is 4 ==> [0, 1, 2, 5, 6, 7, 8]


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)