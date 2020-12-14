from collections import defaultdict


# enumerate all possible integers from the bitstring taking into account X's
# i is the position currently being considered
def en(bs, i=0):
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
    # if this statement sets a mask, set it and continue
    if loc == "mask":
        mask = num
        continue

    # get the memory location as a bitstring from 'mem[123]'
    #
    # loc          = 'mem[123]'
    # loc[4:-1]    = '123'
    # bin(123)     = '0b1111011'
    # bin(123)[2:] = '1111011'
    # '1111011'.rjust(36, '0') = '000000000000000000000000000001111011'
    memloc = bin(int(loc[4:-1]))[2:].rjust(36, '0')

    # apply the mask
    # set to the original character (bc) if the mask at that position is 0, otherwise set to 1 if the mask at that position is 1, otherwise set to X
    res = "".join(bc if mc == "0" else "1" if mc == "1" else "X" for bc, mc in zip(memloc, mask))

    # for each possible integer
    # each mask only has 9 or so X's, so only 512 possible values, meaning brute force is viable
    for ml in en(res, 0):
        # set the corresponding value in memory
        mem[ml] = int(num)

print(sum(mem.values()))
