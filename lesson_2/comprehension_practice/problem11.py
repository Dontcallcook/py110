dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = [char for value in dict1.values()
                       for string in value
                       for char in string if char in 'aeiou']

# for key, value in dict1.items():
#     for lst in value:
#         for string in lst:
#             for char in string:
#                 if char in ['a', 'e', 'i', 'o', 'u']:
#                     list_of_vowels.append(char)
                    


print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']