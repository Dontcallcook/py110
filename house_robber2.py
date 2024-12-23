""" 
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]

grid = [[1, 3]
        [1, 5]

grid = [1, 4]
       [2, x] x should be minimum of number above and number to left + original grid value, so x == 2 (minimum of above and left) + 5 (original grid value) == 7
] """

def min_sum(grid):
    if not grid:
        return 0
    elif len(grid) == 1:
        return sum(grid[0])
    elif len(grid[0]) == 1:
        return sum(num for row in grid for num in row)
    
    minimum_sums = [[num for num in row] for row in grid]

    for i in range(1, len(minimum_sums[0])): # update first row, except first value
        minimum_sums[0][i] = grid[0][i] + minimum_sums[0][i - 1]
    
    for row in range(1, len(minimum_sums)): # update first value of each row, except row 0
        minimum_sums[row][0] = minimum_sums[row - 1][0] + grid[row][0]

    for row in range(1, len(minimum_sums)): # fill in rest of grid
        for i in range(1, len(minimum_sums[0])):
            minimum_sums[row][i] = min(minimum_sums[row - 1][i], minimum_sums[row][i - 1]) + grid[row][i]
    
    return minimum_sums[-1][-1]

print(min_sum([[1, 3, 1],
               [1, 5, 1],
               [4, 2, 1]
]))