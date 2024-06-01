list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]


def interleave(list1, list2):
    idx = 0
    new_list = []
    while idx < len(list1):
        new_list.extend([list1[0], list2[0]])
        idx
    
    return new_list
        
    

print(interleave(list1, list2) == expected)      # True