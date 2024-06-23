def row_maker(requested_row):
        number_list = []
        index = 0
        while index < requested_row:
            number_list.append([])
            index += 1
        return number_list
    

def sum_generator(requested_row):
    number_list = row_maker(requested_row)
    number_list_index = 0
    row = 1
    number = 2
    
    while row <= requested_row:
        number_list[number_list_index].append(number)
        number += 2
        if row == len(number_list[number_list_index]):
            row += 1
            number_list_index += 1

    return sum(number_list[number_list_index - 1])

print(sum_generator(2))

    
    
    
    

    