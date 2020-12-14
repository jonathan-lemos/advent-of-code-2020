from math import ceil
lines = [x.strip() for x in open("input2.txt")]
timestamp = int(lines[0])
buses = [x.strip() for x in lines[1].split(",")]

active_buses = [int(x) for x in buses if x.isdigit()]
moduli = [(x, ceil(timestamp / x) * x) for x in active_buses]
m = min(moduli, key=lambda x: x[1])
print(m[0] * (m[1] - timestamp))
