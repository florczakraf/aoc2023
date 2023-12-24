import re

import math
import sys
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from queue import Queue
import z3


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()
total = 0
hailstone = []


for line in input:
    hailstone.append([int(x) for x in re.findall(r"[-\d]+", line)])


x, y, z, xv, yv, zv = z3.Ints("x y z xv yv zv")
solver = z3.Solver()

for i, h in enumerate(hailstone):
    hx, hy, hz, hxv, hyv, hzv = h
    t = z3.Int(f"t{i}")
    solver.add(t >= 0)
    solver.add(x + xv * t == hx + hxv * t)
    solver.add(y + yv * t == hy + hyv * t)
    solver.add(z + zv * t == hz + hzv * t)

solver.check()
m = solver.model()

x, y, z = m[x].as_long(), m[y].as_long(), m[z].as_long()

print(x + y + z)
