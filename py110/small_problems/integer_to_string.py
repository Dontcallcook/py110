# PROBLEM:
#     - conver an integer to the string representation of that integer.

# RULES:
#     - cannot use built-in string function, str()

# INPUT:
#     -int

# OUTPUT:
#     -string

# DATA_STRUCTURES:
#     - dictionary to store digits as keys and characters as values -> {0:'0'} etc.

# ALGORITHM:
#     - divmod(integer, 10) to return (rest of digits, first digit)
#     - insert digit to first element of list -> list.insert(0, digit)
#     - take remaining integer from divmod output and repeat first two steps
#     - repeat until intger == 0

digit_to_string_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

def integer_to_string(integer):
    digit_list = []
    
    if integer != 0:
        while integer != 0:
            remaining, first = divmod(integer, 10)
            digit_list.insert(0, digit_to_string_dict[first])
            integer = remaining
    
    return ''.join(digit_list) or '0'

# TEST CASES:
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# print(divmod(4321, 10)) -> (432, 1)
# print(divmod(432, 10)) -> (43, 2)
# print(divmod(43, 10)) -> (43, 3)
# print(divmod(4, 10)) -> (0, 4)