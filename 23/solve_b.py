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

visited = set()
g = defaultdict(dict)


def neighbors(y, x):
    candidates = []
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dy, dx in deltas:
        y_ = y + dy
        x_ = x + dx
        if 0 <= y_ < len(input) and 0 <= x_ < len(input[y_]) and input[y_][x_] != "#":
            candidates.append((y_, x_))

    return candidates

start = (0, 1)
end = (len(input) - 1, len(input[0]) - 2)

junctions = set()

for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c != "#":
            ns = neighbors(y, x)
            if len(ns) in (1, 3, 4):
                junctions.add((y, x))

for y, x in junctions:
    candidates = [(y, x)]
    visited = {(y, x)}
    path = 0
    while candidates:
        path += 1
        next_candidates = []
        for (y_, x_) in candidates:
            for y__, x__ in neighbors(y_, x_):
                if (y__, x__) not in visited:
                    visited.add((y__, x__))
                    if (y__, x__) in junctions:
                        g[(y, x)][(y__, x__)] = path
                    else:
                        next_candidates.append((y__, x__))
        candidates = next_candidates

best = 0
visited = {}

sys.setrecursionlimit(100000)
def dfs(y, x):
    global best
    if (y, x) == end:
        if sum(visited.values()) > best:
            best = sum(visited.values())

    for y_, x_ in g[(y, x)]:
        if (y_, x_) not in visited:
            visited[y_, x_] = g[(y, x)][(y_, x_)]
            dfs(y_, x_)
            visited.pop((y_, x_))

dfs(*start)
print(best)
