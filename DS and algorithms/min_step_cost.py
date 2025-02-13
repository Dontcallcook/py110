"""
PROBLEM:
write a function that calculates the steps 
"""

def min_cost(cost):
    dp = [price if i == 0 or i == 1 else 0 for i, price in enumerate(cost)]

    for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    
    return min(dp[-1], dp[-2])

print(min_cost([10, 15, 30, 5, 20, 10, 5]))