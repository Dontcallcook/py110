"""
PROBLEM:
You are climbing a staircase, and it takes n steps to reach the top.
You can climb either 1 step or 2 steps at a time.
You need to determine how many distinct ways there are to reach the top.


def sort_by_exclusion(words):
    strings = words[:]
    dp_array = []
    current_sub = []
    
    while strings:
        if not current_sub or strings[0] > current_sub[-1]:
            current_sub.append(strings.pop(0))
        else:
            dp_array.append(current_sub)
            current_sub = []

    return len(min(dp_array))
"""

import pdb
def sort_by_exclusion(steps):
    if steps == 0:
        return 1
    
    dp = [0 for _ in range(steps + 1)]
    dp[0] = dp[1] = 1

    for i in range(2, steps + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[-1]

print(sort_by_exclusion(0)) # -> [1, 1, 2, 3]