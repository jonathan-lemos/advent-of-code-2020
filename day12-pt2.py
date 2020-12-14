lines = [x.strip() for x in open("input2.txt")]
cmds = [(x[0], int(x[1:])) for x in lines]

wpx, wpy = 10, 1
x, y = 0, 0

for d, num in cmds:
    if d == "N":
        wpy += num
    elif d == "S":
        wpy -= num
    elif d == "E":
        wpx += num
    elif d == "W":
        wpx -= num
    elif d == "R":
        if num == 0:
            pass
        elif num == 270:
            wpx, wpy = -wpy, wpx
        elif num == 180:
            wpx, wpy = -wpx, -wpy
        elif num == 90:
            wpx, wpy = wpy, -wpx
    elif d == "L":
        if num == 0:
            pass
        elif num == 90:
            wpx, wpy = -wpy, wpx
        elif num == 180:
            wpx, wpy = -wpx, -wpy
        elif num == 270:
            wpx, wpy = wpy, -wpx
    elif d == "F":
        x += wpx * num
        y += wpy * num
    else:
        raise Exception()
    print("pos", x, y)
    print("wp", wpx, wpy)
    print()
print(x, y)
print(abs(x) + abs(y))
