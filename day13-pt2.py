lines = [x.strip() for x in open("input2.txt")]
buses = [x.strip() for x in lines[1].split(",")]

expected = []
for i, bus in enumerate(buses):
    if not bus.isdigit():
        continue
    expected.append((int(bus), i))

print(", ".join([str(x[0]) for x in expected]))
print(", ".join([str(x[1]) for x in expected]))

x = expected[0][0]
factor = 1
for num, ind in expected:
    while (x + ind) % num != 0:
        x += factor
    factor *= num
print(x)

