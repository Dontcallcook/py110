# PROBLEM:
#     - write a program that checks if the parenthesis are properly balanced

# RULES:
#     - properly balanced = () (()) etc.
#     - improperly blanaced = )(, ), (, (() etc.
    
#     Imbalanced:
#     - if it starts with a right parenthesis, it is not balanced
#     - if there is only one parenthesis, it is not balanced
#     - if the number of left and right parenthesis are unequal, it is not balanced

# ALGORITHM:
#    - keep track of which side is being counted, left or right
#    - check when one side ends, the other matches it
#    - ("What ((is))) up(")
#    - right: 1, 1
#    - left: 1, 1, 1
#    - left: 1

#    - initiate variables for left and right parenthesis and counted_parenthesis (left or right)
#    - loop over string and count left and right parenthesis
#       - check if the counted parenthesis (left or right) has changed
#       - if it has changed, check the previous count to see if they match
import pdb

PARENTHESES = [("{", "}"), ("[", "]"), ("(", ")")]

def is_balanced(string):
    if string.count("'") % 2 == 1 or string.count('"') % 2 == 1:
        return False

    for pairs in PARENTHESES:
        if string.count(pairs[0]) != string.count(pairs[1]):
            return False

        if string.find(pairs[0]) > string.find(pairs[1]):
            return False

        if string.rfind(pairs[0]) > string.rfind(pairs[1]):
            return False

    return True

# TEST CASES:
print(is_balanced("What (is) this?") == True)
print(is_balanced("What is) this?") == False)
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ((is))) up(") == False)

#FURTHER EXPLORATION:
print(is_balanced("'What (is) this?") == False)
print(is_balanced("'What' (is) this?") == True)
print(is_balanced("'What''' (is) this?") == True)
print(is_balanced('What (is)" this?') == False)
print(is_balanced('What {is} this?') == True)
print(is_balanced('What }{is} this?') == False)
print(is_balanced('What [{]is} this?') == True)