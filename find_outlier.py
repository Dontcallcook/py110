def find_nb(m, n=1):
    total = 1 + (2 ** 3) # 2 layers worth
    layer = 3
    
    while total < m:
        total += layer ** 3
        layer += 1
    
    return layer - 1 if total == m else -1

print(find_nb(4183059834009))