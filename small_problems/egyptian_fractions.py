"""PROBLEM:
    - write a function that takes a rational number (a number that can be expressed as a fraction - > 0.5: 1/2, 0.33333: 1/3, 1: 1/1)
    - and converts it to a list of denominators 1/3 <- denominator
    - e.g., 2, 1 input -> [1, 2, 3, 6] output

    INPUT:
    - rational number fraction -> Fraction(2, 1)

    OUTPUT:
    - list of denominators of unit fractions that equal rational number
    - 1/1, 1/2, 1/3, 1/6 -> [1, 2, 3, 6]

"""

from fractions import Fraction

def unegyptian(denominator_list):
    return sum([Fraction(1, denominator) 
                for denominator in denominator_list])

def egyptian(rational_number):
    unit_fractions = []
    denominator = 1

    while unegyptian(unit_fractions) < rational_number:
        if (unegyptian(unit_fractions) + Fraction(1, denominator) 
           > rational_number):
            denominator += 1
        else:
            unit_fractions.append(denominator)
            denominator += 1

    return unit_fractions
"""
PROBLEM:
- need to find the common denominator of fractions in list
- [1, 2, 3, 6] 

"""


print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
"""
EXAMPLE:
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]

"""



