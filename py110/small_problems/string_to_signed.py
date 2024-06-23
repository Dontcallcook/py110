# PROBLEM:
#     - function doesn't account for signed numbers.
#     - Modify the function to make sure the output is the correct sign

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

def string_to_signed_integer(string):
    total = 0
    multiplier = 1
    idx = -1
    
    if string.startswith("-"):
        while idx > (-len(string)):
            total -= (digits[string[idx]] * multiplier)
            multiplier *= 10
            idx -= 1
    
    elif string.startswith("+"):
        while idx > (-len(string)):
            total += (digits[string[idx]] * multiplier)
            multiplier *= 10
            idx -= 1
    
    else:
        while idx >= (-len(string)):
            total += (digits[string[idx]] * multiplier)
            multiplier *= 10
            idx -= 1

    return total

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True