"""
[[1, 1], 
 [1, 1]]

[[1, 1],
 [1, 2]]

 each cell is equal to dp[k][j][i] = dp[k - 1][j][i] + dp[k][j - 1][i] + dp[k][j][i - 1]
"""

def ways_in_3d_matrix(x, y, z):
    if x == 1 and y == 1:
        return 1
    
    dp = [[[0 for i in range(x)] for j in range(y)] for k in range(z)]
    dp[0][0][0] = 1
    # initialize first layer
    for j in range(y):              
        for i in range(x):
            if i == 0 or j == 0:
                dp[0][j][i] = 1
            else:
                dp[0][j][i] = dp[0][j - 1][i] + dp[0][j][i - 1]
    
        for k in range(1, z):
            for j in range(y):
                for i in range(x):
                    above = dp[k - 1][j][i]
                    left = dp[k][j][i - 1]
                    up = dp[k][j - 1][i]
                    if i == 0 and j == 0:
                        dp[k][j][i] = above
                    elif i == 0:
                        dp[k][j][i] = up
                    else:
                        dp[k][j][i] = left + above + up

    return dp

print(ways_in_3d_matrix(2, 2, 2))