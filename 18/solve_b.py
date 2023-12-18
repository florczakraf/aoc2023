import math
import sys
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from queue import Queue


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

ops = []

for line in input:
    _, __, color = line.split(" ")
    n = int(color[2:-2], 16)
    d = ["R", "D", "L", "U"][int(color[-2:-1], 16)]

    ops.append((d, n, color))

y, x = 0, 0
total = 0
for d, n, _ in ops:
    y_, x_ = y, x
    if d == "R":
        x_ += n
    elif d == "D":
        y_ += n
    elif d == "L":
        x_ -= n
    else:
        y_ -= n

    total += (x * y_) - (x_ * y) + abs(x_ - x + y_ - y)

    y, x = y_, x_


print(total//2 + 1)
