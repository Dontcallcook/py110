"""
PROBLEM:
return the number of identical pairs in a list
pairs are counted once 

EXAMPLE:
[1, 1, 2, 3, 4, 2] => 2
[2, 2, 2, 2, 2] => 2

DATA STRUCTURE:
"""
def calculate_pairs(data):
    pairs = {}
    
    for key, value in data.items():
        if data[key] > 1:
            pairs[key] = data[key] // 2
  
    return pairs

def pairs(lst):
    if not lst:
        return 0
    
    count = {}

    for num in lst:
        count[num] = count.get(num, 0) + 1
    
    pairs = calculate_pairs(count)
    
    return sum(pairs.values())

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)