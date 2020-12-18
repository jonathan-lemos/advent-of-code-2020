lines = [x.strip() for x in open("input2.txt")]


def evaluate(lexemes):
    def peek():
        return lexemes[-1] if len(lexemes) > 0 else None

    def ev_factor():
        c = lexemes.pop()
        if c == "(":
            res = ev_expr()
            assert lexemes.pop() == ")"
            return res
        else:
            return int(c)

    def ev_term():
        r1 = ev_factor()
        if peek() != "+":
            return r1
        lexemes.pop()
        r2 = ev_term()
        return r1 + r2

    def ev_expr():
        r1 = ev_term()
        if peek() != "*":
            return r1
        lexemes.pop()
        r2 = ev_expr()
        return r1 * r2

    return ev_expr()


s = []
for line in lines:
    x = line.split()
    lexemes = list(reversed([b for sublist in [list(a) for a in x] for b in sublist]))

    s.append(evaluate(lexemes))
print(s)
print(sum(s))

