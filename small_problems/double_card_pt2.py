def double_consonants(string):
    doubled = ""
    for char in string:
        if char not in "aeiou" and char.isalpha():
            doubled += char * 2 
        else:
            doubled += char 
        
    return doubled

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")