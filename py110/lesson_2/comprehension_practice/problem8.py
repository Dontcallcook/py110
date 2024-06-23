# write code that creates a list containing the colours of the fruits and sizes of the vegetables
# sizes should be uppercase and colours should be capitalised.

# INPUT:
#     dict

# OUTPUT:
#     list
    
# EXAMPLE:
#     [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# ALGORITHM:
#   loop through dict
#   check if fruit or vegetable
#   if fruit, append colour capitalised to new list
#   if vegetable, append size in uppercase to new list

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_info(info):
        if info['type'] == 'fruit':
            return [color.capitalize() for color in info['colors']]
        else:
            return info['size'].upper()

new_lst = [transform_selection(info) for info in dict1.values()]

print(new_lst)     
        