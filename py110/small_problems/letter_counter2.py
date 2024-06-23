# ALGORITHM:
#     initialize an empty dictionary
#       clean the string
#           - for char in string if not char.alpha() -> replace char with ""
#     split up the string into a list using a space delimiter
#         - ['Hey', 'Job,', 'how', 'are', 'you?']
#     loop through list
#     for each word, calculate the length.
#     check if length of word already in dictionary
#     if the length is not in dictionary keys, assign the length to a dictionary key
#     if the length is in dictionary keys, increment the value of that dictionary key

def word_sizes(string):
    len_dict = {}
    string_list = string.split()
    
    clean_string = ''
    
    for i, word in enumerate(string_list):
        for char in word:
            if char.isalpha():
                clean_string += char
        string_list[i] = clean_string
        clean_string = ''
    
    for word in string_list:
        len_dict[len(word)] = len_dict.get(len(word), 0) + 1
    
    return len_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})