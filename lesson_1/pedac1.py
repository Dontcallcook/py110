sub_list = []

def palindrome_checker(string):
    substring = ""
    i = 0

    while i < len(string):
        word = string[i:]
        for char in word:
            substring += char
            if len(substring) > 1:
                sub_list.append(substring)
        i += 1
        substring = ""
    
    return [substring for substring in sub_list if substring[::-1] == substring]

print(palindrome_checker("repaper"))