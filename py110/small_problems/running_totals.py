# PROBLEM:
#     return a list that consists of the same number of elements as the input list,
#     but the values should be a running total of the sum of the values.

#     RULES:
#         Implicit rules:
#             - empty list returns an empty list

# EXAMPLES:
#     input  -> [1, 2, 3, 4]
#     output -> [1, 3, 6, 10]
                    

# ALGORITHM:
#     1. assign the first value of input_list to output_list
#     2. add second input list element to first output list element - use two indexes?
#     3. add third input list element to second output list element
#     4. repeat while index1 < length of input list

def running_total(data):
    total = 0
    output_list = []
    
    for num in data:
        total += num
        output_list.append(total)

    return output_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
