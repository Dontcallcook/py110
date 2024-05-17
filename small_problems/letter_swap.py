# PROBLEM:
#     Given a string, write a function that returns the string with the first and last letters of every word swapped.
    
#     RULES:
#         Every word has at least one letter
#         each string is nothing but words and single spaces

# INPUT:
#     string

# OUTPUT:
#     string with first and last letters of each word swapped

# EXAMPLES:
#     'Oh what a wonderful day it is' -> 'hO thaw a londerfuw yad ti si'
#     'dog' -> 'god'
#     'd' -> 'd'

# DATA STRUCTURES:
#     string -> string_list
#     swap letters of words in string_list -> join string_list to make string

# ALGORITHM:
#     split the string into words list
#     loop through words in words list
#     for each word, create a new word that consists of slices of the words in words list
#         - swapped_word = old_word[1:] + old_word[0]
#         - replace the word in word list with the swapped_word
#     join words list together
#     return words list

def swap(string):
    words = string.split()
    for i, word in enumerate(words):
        if len(word) < 2:
            words[i] = word
        else:
            swapped_word = word[-1] + word[1:-1] + word[0]
            words[i] = swapped_word
    
    return ' '.join(words)
    


print(swap('Oh what a wonderful day it is') == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True