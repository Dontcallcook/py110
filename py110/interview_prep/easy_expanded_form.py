# expanded_form(12); # Should return '10 + 2'
# expanded_form(42); # Should return '40 + 2'
# expanded_form(70304); # Should return '70000 + 300 + 4'

# Note: All numbers will be whole numbers greater than 0.
"""
PROBLEM:
return the expanded form of a number as a string
the numbers should be separated by a '+'

EXAMPLE:
1 -> '1'
12 -> '10 + 2'
110 -> '100 + 10'
111 -> '100 + 10 + 1'

DATA STRUCTURE:
list to store each separate number of expanded form:

[100, 10, 1]

ALGORITHM:
set multiplier as 1
% 10 the number 
times the remainder by the multiplier
add the result to a list
continue until the number is empty

from the list, create the expanded form string
"""
def expanded_form(num):
    nums = []
    multiplier = 1

    for _ in range(len(str(num))):
        num, remainder = divmod(num, 10)
        remainder *= multiplier
        nums.append(remainder)
        multiplier *= 10

    return ' + '.join([str(num) for num in nums if num > 0][::-1])

print(expanded_form(111))
print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')
