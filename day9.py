from copy import deepcopy
from functools import reduce
import re

lines = [x.strip() for x in open("input2.txt")]
preamble_len = 25

nums = [int(x) for x in lines]

preamble = nums[:preamble_len]
for i in range(preamble_len, len(nums)):
    flag = False
    for j in range(len(preamble)):
        for k in range(j + 1, len(preamble)):
            if nums[i] == preamble[j] + preamble[k]:
                flag = True
                break
        if flag:
            break

    if not flag:
        # print(nums[i])
        # exit(0)
        target = nums[i]
        break

    preamble = preamble[1:]
    preamble.append(nums[i])

for i in range(len(nums)):
    ctr = nums[i]
    for j in range(i + 1, len(nums)):
        if ctr > target:
            continue
        if ctr == target:
            print(min(nums[i:j]) + max(nums[i:j]))
            exit(0)
        ctr += nums[j]


