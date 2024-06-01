# PROBLEM:
#     - write a function that takes two arguments.
#     - first argument is the count -> the number of elements in the final list
#     - the second argument is the multiple. each element should be a multiple of this argument

# EXAMPLE:
#     5, 1 -> [1, 2, 3, 4, 5]
#     3, -8 -> [-8, -16, -24]
    
# ALGORITHM:
#     ititiate multiple

def sequence(num, multiple):
    return [idx * multiple for idx in range(1, num + 1)]

print(sequence(5, 1))          # [1, 2, 3, 4, 5]
print(sequence(4, -7))         # [-7, -14, -21, -28]
print(sequence(3, 0))          # [0, 0, 0]
print(sequence(0, 1000000))    # []
    