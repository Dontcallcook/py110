"""
PROBLEM:
Write a program that returns the minimum number of coins needed to equal the amount argument.

INPUT:
list containing coin values -> [2, 5, 10]
integer representing amount needed -> 7

OUTPUT:
integer representing minimum number of coins -> 2 (one 5 + one 2)

RULES:
You have an infinite amount of each coin
return -1 if the amount cannot be reached

EXAMPLE [1, 2, 4], 4:
dp[i] is the minimum amount of coins needed for a given amount [i] -> dp[1] represents amount 1, dp[2] represents amount 2, etcl. dp init as -> [0, inf, inf]

loop through the coins
    loop through the minimum coins
    (coin 1) for each minimum amount of coins (dp[i]), check if the current coin is less than or equal to the amount [i], and is less than the current value of dp[i]
            coin (1) == [i] (1) and equal the value of coin -> so inf becomes 1
            coin (1) < [i] (2) and twice the value of coin -> so inf becomes 2
            coin (1) < [i] (3) and three times the value of coin -> so inf becomes 3
            coin (1) < [i] (4) and four times the value of coin -> so inf becomes 4
    
    (coin 2) for each minimum amount of coins (dp[i]), check if the current coin is less than or equal to the amount [i], and is less than the current value of dp[i]
            coin (2) > [i] (1) -> so dp[i] (1) stays the same
            coin (2) == [i] (2) -> so dp[i] (2) -> so dp[i] (2) becomes 1
            coin (2) < [i] (3) -> so dp[i] (3) becomes 2
            coin (2) < [i] (4) -> so dp[i] (4) becomes 2 -> dp[i] == 3
    
    (coin 4) for each minimum amount of coins (dp[i]), check if the current coin is less than or equal to the amount [i], and is less than the current value of dp[i]
            coin (4) > [i] (1) -> so dp[i] (1) stays the same
            coin (4) > [i] (2) -> so dp[i] (2) stays the same
            coin (4) > [i] (3) -> so dp[i] (3) stays the same
            coin (4) == [i] (4) -> so dp[i] (4) becomes 1 -> dp[i] == 1

                  coins = [1, 2, 4]
                amounts = [0, 1, 2, 3, 4] 
minimum_amount_of_coins = [0, 1, 2, 3, 4]            

only loop from coin to end of amounts
coin 1 -> minimum_amount_of_coins[value] = min(minimum_amount_of_coins[value], minimum_amount_of_coins[value - coin] + 1)
-> minimum_amount_of_coins = [0, 1, 2, 3, 4]
coin 2 -> minimum_amount_of_coins[value] = min(minimum_amount_of_coins[value], minimum_amount_of_coins[value - coin] + 1)
-> minimum_amount_of_coins = [0, 1, 2, 3, 4]
"""

def min_coins(coins, amount):
    minimum_amount_of_coins = [0 if i == 0 else float('inf') for i in range(0, amount)]
    
    for coin in coins:
        for min_amount in range(coin, len(minimum_amount_of_coins)):
            minimum_amount_of_coins[min_amount] = min(minimum_amount_of_coins[min_amount], minimum_amount_of_coins[min_amount - coin] + 1)
    return minimum_amount_of_coins

print(min_coins([1, 3, 4], 6))