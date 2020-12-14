x = 0
factor = 1
for ind, num in filter(lambda z: z[1] > 0, enumerate(-1 if y == "x" else int(y) for y in (x.strip() for x in list(open("input2.txt"))[1].split(",")))):
    while (x + ind) % num != 0:
        x += factor
    factor *= num
print(x)
