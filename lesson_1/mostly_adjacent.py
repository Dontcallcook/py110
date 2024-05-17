# PROBLEM:
#     - Given a list of strings, create a new list in the order of amount of adjacent consonants.
    
#     Rules:
#         Explicit Rules:
#         - Consonants are adjacent if they are next to each other in word, or between adjacent words
#         - E.G., "Bad Job" -> "d" and "J" are adjacent
#         - If two strings in the list contain the same amount of cosonants, they should retain the same order
        
#         Implicit Rules:
#         - If string has only one vowel, this counts as 0 adjacent, so should keep same order with other 0 adjacent consonant strings
#         - Should be sorted in descending order -> highest to lowest
#         - Can't contain empty strings
#         - Case doesn't matter
#     Input:
#         -  List of strings
#     Output:
#         - list of strings arranged in descending order of most adjacent consonants

# DATA STRUCTURES:
#     - list input
#     - new list output

# ALGORITHM:
#     1. loop through string_input_list.
#     2. For each string in string_input_list, count the number of adjacent consonants
#       - check if char is consonant
#       - if char is consonant assign to temporary string -> consonant_string
#       - check if next char is consonant
#       - if it is a consonant, add it to consonant_string
#       - repeat until a vowel is found
#           - measure the length of consonant_string and add that value to consonant_count
#           - reset consonant_string
#       - repeat process
#     3. Assign the number of adjacent consonants to that word
#         - create a key for the string in a dictionary, and assign consonant_count to that key
#     4. Repeat steps 2-3 for all strings in string_input_list
#     5. Sort the words from highest to lowest count
#     6. Return ordered_consonants_list

VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']

def consonant_counter(string):
    consonant_count = 0
    string = string.replace(" ", "")
    consonant_string = ""
    
    for char in string:
        if char not in VOWEL_LIST:
            consonant_string += char
        else:
            if len(consonant_string) > 1:
                consonant_count += len(consonant_string)
            consonant_string = ''
    if len(consonant_string) > 1:
        consonant_count += len(consonant_string)
    
    return consonant_count

def sort_by_consonant_count(strings):
    sorted_strings = sorted(strings, key=consonant_counter, reverse=True)
    return sorted_strings
    
    
my_list = ['aa', 'baa', 'ccaa', 'dddaa'] # {'aa': '0', 'baa': '0', 'ccaa' : '2', 'dddaa': 3}
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan'] # {'can can': '2', 'toucan': '0', 'batman' : '2', 'salt pan': 3}
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar'] # {'bar': '0', 'car': '0', 'far' : '0', 'jar': 0}
print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year'] # {'month': 3, 'day': 0, 'week': 0, 'year': 0}
print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb'] # {'xxxx': 4, 'xxxa': 3, 'xxxb': 3}
print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']
    