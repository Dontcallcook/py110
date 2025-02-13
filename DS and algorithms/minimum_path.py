""" If I know the minimum path sum to reach the left or above cell, can I use that information to find the minimum path sum to reach the current cell?

if grid[i][j] + dp[i - 1][j] < grid[i][j] + dp[i][j - 1]:
    dp[i][j] = grid[i][j] + dp[i - 1][j]

else:
    dp[i][j] = grid[i][j] + dp[i][j - 1]
 """

def min_sum_path(grid):
    if isinstance(grid[0], list) and len(grid[0]) == 1: # handle single column grid
        return sum([num for row in grid for num in row])
    elif isinstance(grid[0], int): # handle single row grid
        return (sum(grid))

    dp = [[grid[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]
    dp[0][0] = grid[0][0]

    for i in range(1, len(dp[0])):
        dp[0][i] = dp[0][i - 1] + dp[0][i]
    
    for j in range(1, len(dp)):
        dp[j][0] = dp[j - 1][0] + dp[j][0]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = min([dp[i - 1][j] + dp[i][j], dp[i][j - 1] + dp[i][j]])
    
    return dp[-1][-1]


print(min_sum_path([
  [1, 3],
  [1, 5]
])) # 7

print(min_sum_path([
    [1, 2, 3],
    [4, 5, 6]
])) # 35

print(min_sum_path([
    [5, 9, 3],
    [6, 7, 1],
    [4, 8, 2]
])) # 10

print(min_sum_path([1, 2, 3, 4])) # 10