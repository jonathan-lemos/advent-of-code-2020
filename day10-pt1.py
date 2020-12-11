from copy import deepcopy
from functools import reduce
import re

lines = [x.strip() for x in open("input3.txt")]
nums = [int(x) for x in lines]

n1 = 0
n3 = 1

last = 0
for a in sorted(nums):
    diff = a - last
    if diff == 1:
        n1 += 1
    if diff == 3:
        n3 += 1
    last = a

print(n1)
print(n3)
print(n1 * n3)
