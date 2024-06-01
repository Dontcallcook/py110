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

def signed_integer_to_string(integer):
    digit_list = []
    
    if integer != 0:
        positive_int = abs(integer)
        while positive_int != 0:
            remaining, first = divmod(positive_int, 10)
            digit_list.insert(0, digit_to_string_dict[first])
            positive_int = remaining
    if integer < 0:
        digit_list.insert(0, '-')
    if integer > 0:
        digit_list.insert(0, '+')
    
    return ''.join(digit_list) or '0'

# TEST CASES:
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True