
"""
PROBLEM:
Find the most efficient move for a player to make given a list of moves, and move choices (represented by nested lists)

"""

def minimax(tree):
    unnested_tree = []
    stack = tree[:]

    while stack:
        current_element = stack.pop()
        print(f'current element is {current_element}')
 
        if isinstance(current_element, list):
            try:
                unnested_tree.insert(0, max(current_element))
            except TypeError:
                print('insert failed, stack extended')
                stack.extend(current_element)
        
        else:
            unnested_tree.insert(0, current_element)
        print(f'stack is {stack}')
        print(f'unnested_tree is {unnested_tree}')
        print('--------------------------------->')


    return unnested_tree

print(minimax([ [ [ [0,1],[31,9,3,20] ],5,[4,1] ], 1, 2]))