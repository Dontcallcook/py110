"""
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.
"""

def max_sub(lst):
    sub_arrays = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sub_arrays.append(lst[i:j])
    
    return max(sub_arrays, key=sum)

print(max_sub([1, 2, 3, 4]))