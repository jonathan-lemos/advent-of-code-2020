from copy import deepcopy
from functools import reduce
import re
from operator import mul, add

# 1 4         -- 1
# 1 3 5       -- 1
# 1 3 4       -- 2
# 1 2 4       -- 2
# 1 2 3 4 5   -- 7
# 1 2 3 4     -- 4
# 1 2 3       -- 2

lines = [x.strip() for x in open("input3.txt")]
nums = sorted(int(x) for x in lines)
#nums = [17, 18, 19, 20, 23, 24, 25, 28]
dp = [-1 for _ in range(len(nums))]


def solve(i):
    if dp[i] >= 0:
        return dp[i]

    if i == 0:
        dp[0] = 1
        return 1

    cands = []
    for j in range(i - 1, -1, -1):
        if nums[i] - 3 <= nums[j]:
            cands.append(j)

    ways = 0
    for cand in cands:
        ways += solve(cand)
    dp[i] = ways
    return ways

s = 0
while nums[0] <= 3:
    dp = [-1 for _ in range(len(nums))]
    solve(len(dp) - 1)
    s += dp[-1]
    dp = dp[1:]
    nums = nums[1:]

# print(list(zip(range(len(dp)), nums, dp)))
print(s)
