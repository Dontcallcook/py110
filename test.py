"""
PROBLEM:
given two words, return the number of letters you need to remove from either word to make them anagrams


EXAMPLE:
** 'ab', 'a'
** sorted strings == 'ab' 'a'
** 'a' == 'a'? Yes, return difference 'a' and 'ab'

** '
** sorted strings == 'codewars' 'aacehkknrr'


DATA STRUCTURES:
input: two strings
output: number of chars needed to remove and make them anagrams

int to store letters needed to remove


ALGORITHM:

high-level:

set letters_to_remove as 0
** letters_to_remove = 0
** letters_to_remove = 7

sort both words
** 'codewars' & 'hackerrank'

loop first word and compare with second
    check if current char is in second word
        if it is not
            add 1 to letters_to_remove
        else
            remove char from second word

repeat and compare second word to first word

return letters_to_remove

** 'a' -> 'aab'
** 'a' in 'aab'? Yes, remove 'a' from 'aab' -> 'ab'

** 'ab' -> ''
** 'a' in ''? No, +1 to letters to remove
** 'b' in ''? No, +1 to letters to rmove

"""

"""
PROBLEM:
remove duplicates from a list in place


EXAMPLE:
** 'madam'

** (i) == 0, (j) == 4, checking 'm', against 'm'
** match so (i) + 1 and (j) - 1
** (i) == 1, (j) == 3

** (i) == 1, (j) == 3, checking 'a', against 'a'
** match so (i) + 1 and (j) - 1
** (i) == 2, (j) == 2

** (j) not > than (i) loop ends return True



** 'madaam'

** (i) == 0, (j) == 5, checking 'm', against 'm'
** match so (i) + 1 and (j) - 1
** (i) == 1, (j) == 4

** (i) == 1, (j) == 4, checking 'a', against 'a'
** match so (i) + 1 and (j) - 1
** (i) == 2, (j) == 3

** (i) == 2, (j) == 3, checking 'd', against 'a'
** no match so return False


ALGORITHM:
set i as 0 and j as length of string - 1

loop through string until j NOT > i
    check char at string[i] is equal to string[j]
        if equal
            i += 1
            j -= 1
        if not
            return False

return True
"""

# def is_palindrome(string):
#     i, j = 0, len(string) - 1

#     while j > i:
#         if string[i] == string[j]:
#             i += 1
#             j -= 1
#         else:
#             return False
    
#     return True

# print(is_palindrome('madaam'))

"""
PROBLEM:
return the product of all the even digits - the sum of all odd digits in an integer
if there are no even digits, treat product as 1
if there are no odd digits, treat sum as 0


EXAMPLE:
** 12345
** evens == 2, 4, product == 8
** odds == 1, 3, 5, sum == 9
** 8 - 9 == -1

** 246
** evens == 2, 4, 6, product == 48
** odds == None, sum == 0
** 48 - 0 == 48


DATA STRUCTURES:
input: int
output: int

intermediate structures
list to store digits
[1,2,3,4,5]


ALGORITHM:

high-level:
loop through list of digits
    check each to see if it is odd or even
        if odd
            increase `odd_sum` by digit amount
        if even
            multiply `even_product` by digit amount

return `even_product` - `odd_sum`



set odd_sum as 0
** odd_sum == 0, 1, 4, 9

set even_product as 1
** even_product == 1, 2, 8 

loop through list of digits
** [1, 2, 3, 4, 5]
    check each digit to see if odd or even
    ** 1, 2, 3, 4, 5
        if odd
            increase `odd_sum` by digit amount
        if even
            multiply `even_product` by digit amount

return even_product - odd_sum
** 8 - 9 == -1
"""

"""
PROBLEM:
return a list with consecutive duplicates removed


EXAMPLE:
** [1, 1, 2, 2, 1, 3, 3, 3, 2]
** output: [1, 2, 1, 3, 2]


DATA STRUCTURES:
input: list
output: list

intermediate structures:
??


ALGORITHM:

high-level algorithm:

- return False if list empty

- set output list as the first value in input list
** [1, 2, 1, 3, 2]

- loop through input list from 1 to (length of list)
** [1, 2, 2, 1, 3, 3, 3, 2]
    check each value against the last value in output list
        if values are equal
            pass
        else
            add value to output list
    ** 1 == 1? Yes, pass
    ** 2 == 1? No, add 2 to output list
    ** 2 == 2? Yes, pass
    ** 1 == 2? No, add 1 to output list
    ** 3 == 1? No, add 3 to output list
    ** 3 == 3 Yes, pass
    ** 3 == 3 Yes, pass
    ** 2 == 3? No, add 2 to output list
    
- return the output list

"""

"""
PROBLEM:
return the sub sequence that has the highest sum of consecutive prime numbers in a list


EXAMPLE:
** input => [1, 3, 5, 7, 2, 4, 9]
** sub_ list => [[3], [3, 5], [3, 5, 7], [5], [5, 7], [9]]
** output => [3, 5, 7]


DATA STRUCTURES:
input: list
output: list (subsequence)

intermediate structures:
list of prime sublists
** [[3], [3, 5], [3, 5, 7], [5], [5, 7], [7]]


ALGORITHM:

high-level strategy:
loop through with a nested loop to find ALL subsequences
filter subsequences for those that are prime ONLY
calculate sum of each subsequence
    store and update `current_highest_sum_sub`

return `current_highest_sum_sub`


** TEST
** [1, 3, 5, 7, 2, 4, 9]

MAIN
- set `subs` as an empty list
** []

- loop with nested loop to find all subs
** [1, 3, 5, 7, 2, 4, 9]
    - make a slice for each sub
    - check slice to see if all nums are prime with >> HELPER
        - if prime
            add slice to `subs` list

- return max(subs, key=sum)

END

>> HELPER all_prime(lst)
- loop throug the list
** [3, 5, 7]
    check if number is prime with >> HELPER
        if not prime
            return False

return True

END


>> HELPER is_prime(num):
- loop through from 2 -> num with range
** 2, 2
    check if num % value == 0
        if it does
            return False

return True

"""

def is_prime(num):
    if num <= 1:
        return False

    for value in range(2, num):
        if num % value == 0:
            return False

    return True

def all_prime(lst):
    for num in lst:
        if not is_prime(num):
            return False
 
    return True

def max_sum_of_prime_sub(lst):
    subs = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            current_sub = lst[i:j]
            if all_prime(current_sub):
                subs.append(current_sub)

    return max(subs, key=sum)


print(max_sum_of_prime_sub([1, 3, 5, 7, 2, 4, 9]))


print(min(my_dict.items(), key=lambda x:x[1])[0])
