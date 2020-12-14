from collections import defaultdict


def s(bs):
    pos_num = 1
    x_possibilities = 1
    ctr = 0
    for c in bs[::-1]:
        if c == "1":
            ctr += x_possibilities * pos_num
        elif c == "X":
            ctr += x_possibilities * pos_num + ctr
            x_possibilities *= 2
        pos_num *= 2
    return ctr


def en(bs, i):
    if len(bs) - i == 0:
        yield 0
        return
    pos = 2 ** (len(bs) - i - 1)
    if bs[i] == "X":
        r = list(en(bs, i + 1))
        yield from r
        yield from (x + pos for x in r)
    elif bs[i] == "1":
        yield from (x + pos for x in en(bs, i + 1))
    else:
        yield from en(bs, i + 1)


lines = [x.strip() for x in open("input2.txt")]
mask = lines[0].split(" = ")[1]
mem = defaultdict(int)



for loc, num in [x.split(" = ") for x in lines[1:]]:
    if loc == "mask":
        mask = num
        continue

    memloc = bin(int(loc[4:-1]))[2:].rjust(36, '0')
    b = int(num)

    res = ""
    for (bc, mc) in zip(memloc, mask):
        if mc == "0":
            res += bc
        elif mc == "1":
            res += "1"
        else:
            res += "X"

    for ml in en(res, 0):
        mem[ml] = int(num)

print(sum(mem.values()))

