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
q = Queue()
visited = {}
total = 0

for y, line in enumerate(input):
    try:
        x = line.index("S")
        q.put((y, x, 0))
        break
    except ValueError:
        continue

target_steps = 64

while not q.empty():
    y, x, d = q.get()
    if (y, x) in visited:
        continue
    if d == target_steps + 1:
        break
    visited[(y, x)] = d
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        y_ = y + dy
        x_ = x + dx
        if y_ < 0 or y_ >= len(input) or x_ < 0 or x_ >= len(input[y_]) or (y_, x_) in visited:
            continue
        if input[y_][x_] in ".S" and (y_, x_) not in visited:
            q.put((y_, x_, d+1))

for d in visited.values():
    if d % 2 == 0:
        total += 1

print(total)
