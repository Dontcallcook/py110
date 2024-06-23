import pdb

def group_ints(lst, key):
    # pdb.set_trace()
    switch = None
    grouped = []
    new_lst = []
    
    if len(lst) == 0:
        return []
    elif lst[0] < key:
        switch = 'lesser'
    else:
        switch = 'greater'
    
    for num in lst:
        if num < key:
            if switch == 'greater':
                grouped.append(new_lst)
                new_lst = []
                switch = 'lesser'
            new_lst.append(num)
        
        elif num >= key:
            if switch == 'lesser':
                grouped.append(new_lst)
                new_lst = []
                switch = 'greater'
            new_lst.append(num)
    
    grouped.append(new_lst)
    
    return grouped
                  
                  
                
        

    

print(group_ints([1, 2, 3], 0))

"""
ALGORITHIM:
- check first number to see if it's greater or lesser than key
- assign a control variable switch that will track whether the current list is lesser values or greater values
- add values to the list as long as the numbers continue to be either lesser or greater
- if the type of value changes, change the switch, add list to grouped_ints, and start a new list
- repeat until values change again or the end of the list is reached

"""