# PROBLEM:
#     - Write a program that converts a string number into an integer without using built-in functions, such as int()
    
# RULES:
#     - Cannot use int() function

# INPUT:
#     - string

# OUTPUT:
#     - int

# EXAMPLES:
#     - '521' -> 521
#     - '000' -> 0

# TEST CASES:
#     - print(string_to_integer("4321") == 4321)  # True
#     - print(string_to_integer("570") == 570)    # True

# DATA STRUCTURES:
#     - strings
#     - ints

# ALGORITHM:
#     1 initialize total variable
#     2 check string's last number
#     3 take last number * 1 and then add onto total
#     4 * multiplier by 10
#     5 repeat 2-4 until all elements of string sequence are processed

digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def string_to_integer(string):
    total = 0
    multiplier = 1
    idx = -1
    
    while idx >= (-len(string)):
        total += (digits[string[idx]] * multiplier)
        multiplier *= 10
        idx -= 1

    return total

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True