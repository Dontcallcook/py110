lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

ordered_lst = [sorted(sublst) for sublst in lst]

print(ordered_lst)