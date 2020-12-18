lines = [x.strip() for x in open("input2.txt")]


def evaluate(lexemes):
    def ev(begin, end):
        acc = 0
        op = "+"
        i = begin
        while i < end:
            if lexemes[i] == "(":
                ct = 1
                j = i
                while ct > 0:
                    j += 1
                    if lexemes[j] == "(":
                        ct += 1
                    elif lexemes[j] == ")":
                        ct -= 1
                num = ev(i + 1, j)
                i = j
            else:
                num = int(lexemes[i])
            i += 1
            if op == "+":
                acc += num
            else:
                acc *= num
            op = lexemes[i] if i < end else None
            i += 1

        return acc
    return ev(0, len(lexemes))


s = []
for line in lines:
    x = line.split()
    lexemes = [b for sublist in [list(a) for a in x] for b in sublist]

    s.append(evaluate(lexemes))
print(s)
print(sum(s))
