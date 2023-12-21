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
visited = set()

for y, line in enumerate(input):
    try:
        x = line.index("S")
        visited.add((y, x))
        break
    except ValueError:
        continue

target_steps = 26501365
target_mod = target_steps % len(input)
targets = [target_mod, target_mod + len(input), target_mod + len(input) * 2]
ns = []
for i in range(3 * len(input)):
    next_visited = set()
    if i in targets:
        targets.remove(i)
        ns.append(len(visited))
        if not targets:
            print(ns)
            break
    for y, x in visited:
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y_ = (y + dy) % len(input)
            x_ = (x + dx) % len(input)
            if input[y_][x_] in ".S":
                next_visited.add((y + dy, x + dx))
    visited = next_visited
target = target_steps // len(input)
print(
ns[0] + target * ns[1] - target * ns[0] + target * (target - 1) * ((ns[2] - 2 * ns[1] + ns[0]) // 2))
