# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

"""
PROBLEM:
return the longest alphabetical substring

DATA STRUCTURE:
list to store substrings

ALGORITHM:
create all possible substrings of input string

filter substrings to find which are alphabetical
    - loop through string
    - check if next character is greater than current character
        - if not greater:
            - return False
    - if loop finishes return True

sort the list by length
return the longest (last item in the list)
"""

def is_alphabetical(string):
    for i in range(len(string) - 1):
        if string[i + 1] < string[i]:
            return False

    return True

def longest(string):
    subs = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            current_slice = string[i:j]
            if is_alphabetical(current_slice):
                subs.append(current_slice)

    return max(subs, key=len)

print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')
print(is_alphabetical('c'))