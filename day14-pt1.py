from collections import defaultdict

lines = [x.strip() for x in open("input2.txt")]
mask = lines[0].split(" = ")[1]
mem = defaultdict(int)

for loc, num in [x.split(" = ") for x in lines[1:]]:
    if loc == "mask":
        mask = num
        continue

    memloc = int(loc[4:-1])
    b = bin(int(num))[2:].rjust(36, '0')

    res = ""
    for (bc, mc) in zip(b, mask):
        if mc == "X":
            res += bc
        else:
            res += mc

    mem[memloc] = int(res, 2)

print(sum(mem.values()))
