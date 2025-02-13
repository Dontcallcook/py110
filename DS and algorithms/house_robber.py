"""
PROBLEM:
write a function that reutrn the maximum amount of cash you can rob from houses on a street given as an array.
Two adjacent houses cannot be robbed without triggering security.
"""

def robbing_plan(houses):
    if not houses:
        return 0
    elif len(houses) < 3:
        return max(houses)

    dp = houses[:]

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

    return dp[-1]

print(robbing_plan([10, 15, 20, 25])) # [2, ] -> 204