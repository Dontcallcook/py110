""" 
6lb knapsack
               0  1  2  3  4  5  6 lbs      0  1  2  3  4  5  6 lbs
None         [ 0, 0, 0, 0, 0, 0, 0]       [ 0, 0, 0, 0, 0, 0, 0]
water(3,10)  [ 0, 0, 0, 0, 0, 0, 0]       [ 0, 0, 0,10,10, 0, 0]
book(1,3)    [ 0, 3, 0, 0, 0, 0, 0]       [ 0, 3, 3,10,13, 0, 0]
food(2,9)    [ 0, 3, 0, 0, 0, 0, 0]       [ 0, 3, 9,12,13, 0, 0]
jacket(2,5)  [ 0, 3, 0, 0, 0, 0, 0]       [ 0, 3, 9,12,14, 0, 0]
camera(1,6)  [ 0, 6, 0, 0, 0, 0, 0]       [ 0, 6, 9,15, 0, 0, 0]

remaining item weight from dp is = dp[-1][col - item_weights[col - 1]]
it's trying to add two of each item
"""

def knapsack(item_weights, item_values, capacity):
    dp = [[0] * (capacity + 1) for weight in range(len(item_weights) + 1)]
    
    for col in range(2, len(dp) + 1):
        for row in range(1, len(dp)):
            remaining_weight =  col - item_weights[row - 1]
            if item_weights[row - 1] <= col:
                dp[row][col] = max(item_values[row - 1] + dp[row - 1][remaining_weight], dp[row-1][col])
            else:
                dp[row][col] = dp[row - 1][col]

    return dp[-1][-1]

print(knapsack([3, 1, 2, 2, 1], [10, 3, 9, 5, 6], 6))


