# PROBLEM:
#     Write a function that returns the next featured number greater than the integer.
#     if there is no greater featured number, return 'error'

# RULES:
#     Featured numbers are:
#         - odd numbers
#         - multiples of 7
#         - each digit occurs only once, e.g., 49 is featured, 133 is not featured
import pdb

error = ("There is no possible number that "
         "fulfills those requirements.")

def not_odd_number(num):
    return num % 2 == 0

def not_multiple_of_7(num):
    return num % 7 != 0

def is_too_big(num):
    return num >= 9876543201

def not_unique_digits(num):
    return len(list(str(num))) != len(set(str(num)))

def featured(num):
    start_value = num

    if is_too_big(num):
        return error

    while (not_odd_number(num) 
          or not_multiple_of_7(num) 
          or not_unique_digits(num) 
          or num == start_value):
        if not not_multiple_of_7(num):
            num += 7
        elif not not_multiple_of_7(num) and not not_odd_number(num):
            num += 14
        else:
            num += 1

    return num



print(featured(12) == 21)                  # True
print(featured(20) == 21)                  # True
print(featured(21) == 35)                  # True
print(featured(997) == 1029)               # True
print(featured(1029) == 1043)              # True
print(featured(999999) == 1023547)         # True
print(featured(999999987) == 1023456987)   # True
print(featured(9876543186) == 9876543201)  # True
print(featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that "
#          "fulfills those requirements.")
print(featured(9876543201) == error)       # True