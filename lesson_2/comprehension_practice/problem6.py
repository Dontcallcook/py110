lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# for item in lst:
#     for key, value in item.items():
#         item[key] += 1

new_lst = [{key: value + 1 for key, value in dictionary.items()} for dictionary in lst]

print(new_lst)