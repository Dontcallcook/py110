# given a string, return a new string consitsting of every other word of the original string.

# INPUT:
# string

# OUTPUT:
# string

# EXAMPLES:
# "Hello Job." -> ["Hello", "Job"]

# ALGORITHM:
# split string into list of words
# clean words of punctuation
# return a list of only the even indexed words


def every_other(string):
    string_list = string.split()
    return ([word.strip(".,:;?!")
            for i, word in enumerate(string_list)
            if i % 2 == 0])

print(every_other("Hello Job. What's your name? Lovely day today, isn't it?"))