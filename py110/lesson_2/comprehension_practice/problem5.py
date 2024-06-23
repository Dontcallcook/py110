lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_numbers(data):
    return sum([num for num in data if num % 2 == 1])
    
ordered_list = sorted(lst, key=odd_numbers)

print(ordered_list)