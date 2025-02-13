"""
PROBLEM:
return string with every other character in every third word as uppercase

EXAMPLE:

DATA STRUCTURE:
list to store words [Lorem, Ipsum, is, simply, dummy, text, of, the, printing, world]

ALGORITHM:
split sentence into words --> sentence.split()
set index as 1

loop through split list
    check if index is a multiple of 3
    if index is a multiple of 3
        change every other character to uppercase
    increase index by 1
"""
def second_char_upper(word):
    word = list(word)

    for i in range(1, len(word), 2):
        word[i] = word[i].upper()

    return ''.join(word)

def to_weird_case(words):
    words = words.split()
    idx = 1

    for i, word in enumerate(words):
        if idx % 3 == 0:
            words[i] = second_char_upper(words[i])
        idx += 1
    
    return ' '.join(words)



original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)