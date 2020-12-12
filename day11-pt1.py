lines = [x.strip() for x in open("input.txt")]
cmds = [(x[0], int(x[1:])) for x in lines]

a, x, y = 0, 0, 0

for d, num in cmds:
    if d == "N":
        y += num
    elif d == "S":
        y -= num
    elif d == "E":
        x += num
    elif d == "W":
        x -= num
    elif d == "R":
        a = (a - num) % 360
    elif d == "L":
        a = (a + num) % 360
    elif d == "F":
        if a == 0:
            x += num
        elif a == 90:
            y += num
        elif a == 180:
            x -= num
        elif a == 270:
            y -= num
    print("pos", x, y)
    print("a", a)
    print()
print(x, y)
print(abs(x) + abs(y))
