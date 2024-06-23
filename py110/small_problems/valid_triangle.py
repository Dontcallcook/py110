import pdb
        
def triangle(*sides):
    sorted_lengths = sorted([sides[0], sides[1], sides[2]])
    
    if any(arg == 0 for arg in sides):
        return 'invalid'
    elif (sorted_lengths[0] + sorted_lengths[1]) < sorted_lengths[2]:
        return 'invalid'
    
    else:
        if sides[0] == sides[1] == sides[2]:
            return 'equilateral'
        
        elif (sides[0] != sides[1] 
              and sides[1] != sides[2] 
              and sides[2] != sides[0]):
            return 'scalene'

        else:
            return 'isosceles'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True