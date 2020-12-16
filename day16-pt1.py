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


ct = 0
for line in groups[2][1:]:
    ints = [int(x) for x in line.split(",")]
    for n in ints:
        if not any(isvalid(n, key) for key in entry_valid):
            ct += n

print(ct)
