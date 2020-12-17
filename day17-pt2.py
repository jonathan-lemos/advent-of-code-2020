from collections import defaultdict
from itertools import product
from copy import deepcopy

lines = [x.strip() for x in open("input2.txt")]

cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "."))))

ghl, ghr, gtop, gbot, gback, gfront, gleft, gright = -1, 1, -1, 1, -1, len(lines), -1, len(lines[0])

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        cube[0][0][i][j] = c

for _ in range(6):
    old = deepcopy(cube)

    def apply(q, i, j, k):
        neighbors = [(q + w, i + x, j + y, k + z) for w, x, y, z in product([-1, 0, 1], repeat=4) if (w, x, y, z) != (0, 0, 0, 0)]
        active_neighbors = sum(1 for q, x, y, z in neighbors if old[q][x][y][z] == "#")

        if old[q][i][j][k] == "#":
            cube[q][i][j][k] = "#" if active_neighbors in [2, 3] else "."
        else:
            cube[q][i][j][k] = "#" if active_neighbors == 3 else "."

    for q in range(ghl, ghr + 1):
        for i in range(gtop, gbot + 1):
            for j in range(gback, gfront + 1):
                for k in range(gleft, gright + 1):
                    apply(q, i, j, k)


    ghl -= 1
    ghr += 1
    gtop -= 1
    gbot += 1
    gleft -= 1
    gright += 1
    gback -= 1
    gfront += 1

count = sum(1 for q in cube for i in cube[q] for j in cube[q][i] for k in cube[q][i][j] if cube[q][i][j][k] == "#")
print(count)
