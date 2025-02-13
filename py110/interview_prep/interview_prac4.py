"""
PROBLEM:
return a tuple of the closest numbers in a list

EXAMPLE:

DATA STRUCTURE:
int to store current closest value

ALGORITHM:
loop through all possible pairs
    check each pair for closeness
        if closer than current closest
            closest becomes current
"""
def get_closeness(pair):
    return max(pair) - min(pair)

def closest_numbers(lst):
    current_closest = None
    current_closest_value = float('inf')

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            comparison_value = get_closeness((lst[i], lst[j]))
            if comparison_value < current_closest_value:
                current_closest_value = comparison_value
                current_closest = (lst[i], lst[j])
    
    return tuple(current_closest)

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))