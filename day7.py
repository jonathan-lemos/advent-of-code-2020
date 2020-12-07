import re
from collections import defaultdict

lines = [x.strip() for x in open("input.txt")]

c = defaultdict(dict)

for line in lines:
    line = line[:-1]
    lhs, rhs = line.split(" contain ")
    lhs = re.sub(r"\s*bags?", "", lhs)
    if rhs == "no other bags":
        pass
    else:
        r = [re.sub(r"\s*bags?", "", x) for x in rhs.split(", ")]
        for rr in r:
            mat = re.match(r"^(\d+) (.*)$", rr)
            ct = int(mat.group(1))
            col = mat.group(2)
            c[lhs][col] = ct

"""
has = {"shiny gold"}
while True:
    hlen = len(has)
    for key in c:
        for col in c[key]:
            if col in has:
                has.add(key)
    if hlen == len(has):
        break
"""

def solve(col):
    ct = 1
    for ncol in c[col]:
        ct += c[col][ncol] * solve(ncol)
    return ct

# print(len(has) - 1)
print(solve("shiny gold") - 1)
