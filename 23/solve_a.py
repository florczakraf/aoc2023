import re

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
total = 0

slopes = {
    ">": (0, 1),
    "v": (1, 0),
}

def neighbors(y, x):
    c = input[y][x]
    candidates = []
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if c in slopes:
        deltas = [slopes[c]]

    for dy, dx in deltas:
        y_ = y + dy
        x_ = x + dx
        if 0 <= y_ < len(input) and 0 <= x_ < len(input[y_]) and input[y_][x_] != "#":
            candidates.append((y_, x_))

    return candidates

start = (0, 1)
end = (len(input) - 1, len(input[0]) - 2)

best = 0
visited = set()

sys.setrecursionlimit(100000)
def dfs(y, x):
    global best
    if (y, x) == end:
        if len(visited) > best:
            best = len(visited)

    for y_, x_ in neighbors(y, x):
        if (y_, x_) not in visited:
            visited.add((y_, x_))
            dfs(y_, x_)
            visited.remove((y_, x_))

dfs(*start)
print(best)
