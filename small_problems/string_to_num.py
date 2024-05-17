# PROBLEM:
#     convert a string of numbers to an integer without using the built-in funtion int
    
# INPUT:
#     string
# OUTPUT:
#     integer

# DATA STRUCTURES:
#     separate each digit into an element of a list?

# ALGORITHM:
#     initialize variable to track total value
#     extract first digit by slicing -> digit[0:1]
#     with the first digit, times by 10 until value reached:
#       This should be (len(original_string) - 1) times
#       4000 -> 4 -> times by 10 (len(original_string) - 1) times, which is 3 times
#     add value to total
#     repeat for next character of string
    

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
    '9': 9,
}

def string_to_integer(string):
    total = 0
    
    slice_counter = 0
    while slice_counter < len(string):
        digit = digits[string[slice_counter]]
        multiplication_counter = len(string[slice_counter:]) - 1
        
        while multiplication_counter > 0:
            digit = digit * 10
            multiplication_counter -= 1
    
        total += digit
        slice_counter += 1
    
    return total

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True