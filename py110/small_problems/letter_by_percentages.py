# PROBLEM:
#     Write a function that returns the percentages of:
#         1. lowercase characters
#         2. uppercase characters
#         3. neither (not .isalpha())

# RULES:
#     Input always contains at least one character

# INPUT:
#     String 

# OUTPUT:
#     dictionary containing percentages of:
#         1. lowercase characters
#         2. uppercase characters
#         3. neither (not .isalpha())

# DATA STRUCTURES:
#     dictionary to store count then convert to percentage at the end 

# ALGORITHIM:
#     initialise dictionary to store results with keys for each type of character (lowercase, uppercase, neither)
#     loop through the characters of the string and check for each case: lower, upper, neither
#     add one to count in dictionary depending on check
    
#     after loop, convert dictionary value to letter_percentages:
#         - multiply count by length of string (count * len(s) * 100)
#         - convert to 2dp (str(f'{percentage:.2f}'))
    
#     return dictionary

def make_percentage_string(s, percentages):
    for key, value in percentages.items():
        percentages[key] = str(f'{(value / len(s)) * 100:.2f}')
    
    return percentages


def letter_percentages(s):
    # pdb.set_trace()
    percentages = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0,
    }

    for char in s:
        if char.islower():
            percentages['lowercase'] += 1
        elif char.isupper():
            percentages['uppercase'] += 1
        else:
            percentages['neither'] += 1
    
    percentages = make_percentage_string(s, percentages)

    return percentages

# TEST CASES:
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
