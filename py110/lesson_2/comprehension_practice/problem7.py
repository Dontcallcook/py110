lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def multiple_of_three(sublist):
    return [num for num in sublist if num % 3 == 0]

new_lst = [multiple_of_three(sublist) for sublist in lst]

print(new_lst)