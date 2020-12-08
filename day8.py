from copy import deepcopy

lines = [x.strip() for x in open("input.txt")]

r = [x.split() for x in lines]


def run_prog(toggle):
    seen = []
    q = deepcopy(r)
    tmp = q[toggle][0]
    if tmp == "acc":
        return
    q[toggle][0] = "nop" if tmp == "jmp" else "jmp"

    acc = 0
    cur = 0
    while True:
        if cur in seen:
            return

        if cur >= len(q):
            print(acc)
            exit(0)

        seen.append(cur)

        instr, arg = q[cur]
        if instr == "acc":
            acc += int(arg)
            cur += 1
        elif instr == "jmp":
            cur += int(arg)
        else:
            cur += 1


for i in range(len(r)):
    run_prog(i)

