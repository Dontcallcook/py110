def not_valid_triangle(*angles):
    if (angles[0] + angles[1] + angles[2] == 180
       and all(angle > 0 for angle in angles)):
        return False
    
    return True

def triangle(*angles):
    if not_valid_triangle(*angles):
        return 'invalid'
    else:
        if any(angle == 90 for angle in angles):
            return 'right'
        elif all(angle < 90 for angle in angles):
            return 'acute'
        elif any(angle > 90 for angle in angles):
            return 'obtuse'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True