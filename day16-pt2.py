lines = [x.strip() for x in open("input2.txt")]
groups = [[]]
for line in lines:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)

entry_valid = {}
for line in groups[0]:
    typ, expr = [x.strip() for x in line.split(":")]
    r1, r2 = [[int(z) for z in x.split("-")] for x in expr.split(" or ")]
    entry_valid[typ] = [r1, r2]


def isvalid(n, key):
    return any(a[0] <= n <= a[1] for a in entry_valid[key])


def isanyvalid(n):
    return any(isvalid(n, key) for key in entry_valid)


tickets = [[int(x) for x in y.split(",")] for y in [groups[1][1]] + groups[2][1:]]
cols = []


tickets = [t for t in tickets if all(isanyvalid(n) for n in t)]


for col in range(len(tickets[0])):
    cols.append(set())
    for key in entry_valid:
        nums = [t[col] for t in tickets]
        mapping = [(num, isvalid(num, key)) for num in nums if not isvalid(num, key)]
        if all(isvalid(t[col], key) for t in tickets):
            cols[-1].add(key)

while True:
    changed = False
    l1 = set()
    for i in range(len(cols)):
        if len(cols[i]) == 1:
            l1.add(list(cols[i])[0])
    for i in range(len(cols)):
        if len(cols[i]) != 1:
            tmp = len(cols[i])
            cols[i] = cols[i] - l1
            if tmp != len(cols[i]):
                changed = True
    if not changed:
        break

c = [list(x)[0] for x in cols]

a = 1
for i, key in enumerate(c):
    if not key.startswith("departure"):
        continue
    a *= tickets[0][i]

print(a)
