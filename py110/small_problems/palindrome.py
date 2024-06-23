# PROBLEM:
#     write a function that prints True if the string is a palindrome, False otherwise.
    
#     Explicit rules:
#         - string must read the same forwards and back.
#     Implicit rules:
#         - string can include spaces
#         - capitalisation matters
#         - can include numbers

# EXAMPLES:
# print(is_palindrome("madam a madam")) == True)

# ALGORITHM:
#     - compare string to reversed string


def is_palindrome(string):
    return string == string[::-1]


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)