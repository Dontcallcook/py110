lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

ordered_lst = [sorted(sublist, key=str) for sublist in lst]

print(ordered_lst)