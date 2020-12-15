from collections import defaultdict
nums = [int(x) for x in open("input2.txt").read().strip().split(",")]
lastspoken = defaultdict(list)
for i, x in enumerate(nums):
    lastspoken[x] = [i + 1]

last = nums[-1]
for turn in range(len(nums) + 1, 30000001):
    if len(lastspoken[last]) <= 1:
        last = 0
    else:
        last = lastspoken[last][-1] - lastspoken[last][-2]
    lastspoken[last].append(turn)

print(last)

