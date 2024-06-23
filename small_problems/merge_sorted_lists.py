import pdb

def sort_list(data, swaps_made=True):
    while swaps_made:
        swaps_made = False

        for i, num in enumerate(data):
            if data[i] == data[-1]:
                break
            elif data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaps_made = True

    return data

def merge(*data):
    combined_list = [item for seq in data for item in seq]
    sorted_list = sort_list(combined_list)

    return sorted_list

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)