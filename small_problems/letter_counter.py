# PROBLEM:
#     Write a function that takes a string and returns a dictionary that documents the number of words of different lengths.
    
#     Rules:
#         - can be an empty string
#         - punctuation is included in word length

# INPUT:
#     - a string of words

# OUTPUT:
#     - a dictionary documenting the amount of different word lengths 

# EXAMPLES:
#     'Hey diddle diddle, the cat and the fiddle!' -> {3: 5, 6: 1, 7: 2}
#     '' -> {}
#     'Hey Job, how are you?' -> {3: 3, 4: 2}
    
# ALGORITHM:
#     initialize an empty dictionary
#     split up the string into a list using a space delimiter
#         - ['Hey', 'Job,', 'how', 'are', 'you?']
#     loop through list
#     for each word, calculate the length.
#     check if length of word already in dictionary
#     if the length is not in dictionary keys, assign the length to a dictionary key
#     if the length is in dictionary keys, increment the value of that dictionary key

word = 'Hey Job, how are you?'

def word_sizes(string):
    len_dict = {}
    string_list = string.split()

    for word in string_list:
        len_dict[len(word)] = len_dict.get(len(word), 0) + 1
            
    return len_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

