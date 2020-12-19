# https://github.com/jonathan-lemos/eggen-compilers-archive/blob/master/p2/grammar.py
from grammar import grammar

lines = [x.strip() for x in open("input2.txt")]

groups = [[]]
for line in lines:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)


# for part 1, just return s
def rpl(s):
    if s.startswith("8:"):
        return "8: 42 | 42 8"
    if s.startswith("11:"):
        return "11: 42 31 | 42 11 31"
    return s


rules = [x.replace(":", " ->").replace('"', "") for x in map(rpl, sorted(groups[0]))]
gram = grammar(rules)

ct = 0
for ip in groups[1]:
    tokens = [(x, x) for x in ip]
    ast = gram.parse(tokens)
    print(ip, ast)
    if ast is not None:
        ct += 1
print(ct)

