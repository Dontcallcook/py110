# 1. store target as square layer number
# 2. increase layer number by 1
# 3. repeat target == bonus // price

# layer 1 = bonus is 16
# layer 2 = bonus is 4

import pdb

def beeramid(bonus, price, layer=1):
    if bonus == 0:
        return f'number of layers is {layer - 1}'
    else:
        return beeramid(bonus-(price*(layer**2)), price, layer=layer + 1)

print(beeramid(20, 4))# == 5
print(beeramid(1500, 10))