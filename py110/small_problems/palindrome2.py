def punct_stripper(string):
    cleaned_string = ""
    for char in string:
        if char.isalnum():
            cleaned_string += char
    return cleaned_string
        

def is_real_palindrome(string):
    string = punct_stripper(string)
    return string.casefold() == string[::-1].casefold()
    


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

    