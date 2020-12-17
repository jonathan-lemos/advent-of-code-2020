from collections import defaultdict
from itertools import product
from copy import deepcopy

lines = [x.strip() for x in open("input2.txt")]

cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: ".")))

def debug_cube_string():
    return "\n\n".join(f"z={i}:\n" +
                     "\n".join(
                         "".join(cube[i][j][k] for k in sorted(cube[i][j]))
                            for j in sorted(cube[i]))
                         for i in sorted(cube))

gtop, gbot, gback, gfront, gleft, gright = -1, 1, -1, len(lines), -1, len(lines[0])

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        cube[0][i][j] = c

for _ in range(6):
    old = deepcopy(cube)

    def apply(i, j, k, sg = False):
        neighbors = [(i + x, j + y, k + z) for x, y, z in product([-1, 0, 1], repeat=3) if (x, y, z) != (0, 0, 0)]
        active_neighbors = sum(1 for x, y, z in neighbors if old[x][y][z] == "#")

        if old[i][j][k] == "#":
            r = "#" if active_neighbors in [2, 3] else "."
            cube[i][j][k] = r
            return r
        else:
            r = "#" if active_neighbors == 3 else "."
            cube[i][j][k] = r
            return r


    for i in range(gtop, gbot + 1):
        for j in range(gback, gfront + 1):
            for k in range(gleft, gright + 1):
                apply(i, j, k, True)

    print(debug_cube_string())

    gtop -= 1
    gbot += 1
    gleft -= 1
    gright += 1
    gback -= 1
    gfront += 1

count = sum(1 for i in cube for j in cube[i] for k in cube[i][j] if cube[i][j][k] == "#")
print(count)

