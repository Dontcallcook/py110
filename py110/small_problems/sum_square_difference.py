# use a range to create a list consisting of ramge(1, input number + 1)
# work out square of sum: 
#     - use the list to perform each sum -> for num in lst: add to a running total
#     - then ** 2
# work out sum of squares:
#     - use the list to perform each square ->  for num in lst: square and add to a running total
# subtract the final totals and return the value

def sum_squared(num_lst):
    return sum([num for num in num_lst])**2

def sum_squares(num_lst):
    return sum(num**2 for num in num_lst)

def sum_square_difference(num):
    num_lst = [num for num in range(1, num + 1)]

    return sum_squared(num_lst) - sum_squares(num_lst)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True