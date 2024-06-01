# PROBLEM:
#     - function should multiply all values in list together then divide by number values
#     - the result should be a string with the value rounded to three dp

# INPUT:
#     - list

# OUTPUT:
#     - string of float rounded to 3dp

# ALGORITHM:
#     - initiate running total variable assigned the value 1
#     - loop through input list and multiply number by running total
#     - divide running total by length of list

# DATA STRUCTURES:
#     - 

lst = [3, 5]

total = 1

def multiplicative_average(lst):
    total = 1
    for num in lst:
        total *= num

    average = total / len(lst)
    return f"{average:.3f}"

# TEST CASES:
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")