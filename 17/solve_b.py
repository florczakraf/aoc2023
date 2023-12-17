import sys
from collections import defaultdict
from pprint import pprint
import heapq

import math


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()
distances = defaultdict(lambda: math.inf)
q = []

def generate(y, x, d, n):
    candidates = []
    if d is None:
        return [(y, x + 1, "r", 0), (y + 1, x, "d", 0), (y, x - 1, "l", 0), (y - 1, x, "u", 0)]
    elif d == "r":
        if n > 2: candidates.extend([(y-1, x, "u", 0), (y+1, x, "d", 0)])
        if n < 9: candidates.append((y, x + 1, "r", n + 1))
    elif d == "d":
        if n > 2: candidates.extend([(y, x-1, "l", 0), (y, x+1, "r", 0)])
        if n < 9: candidates.append((y + 1, x, "d", n + 1))
    elif d == "l":
        if n > 2: candidates.extend([(y-1, x, "u", 0), (y+1, x, "d", 0)])
        if n < 9: candidates.append((y, x - 1, "l", n + 1))
    elif d == "u":
        if n > 2: candidates.extend([(y, x-1, "l", 0), (y, x+1, "r", 0)])
        if n < 9: candidates.append((y - 1, x, "u", n + 1))

    return candidates


distances[(0, 0, None, 0)] = 0
heapq.heappush(q, (0, (0, 0, None, 0)))
while q:
    dist, (y, x, d, n) = heapq.heappop(q)
    candidates = generate(y, x, d, n)
    for candidate in candidates:
        y_, x_, d_, n_ = candidate
        if y_ < 0 or y_ >= len(input) or x_ < 0 or x_ >= len(input[y_]):
            continue

        new_dist = distances[(y, x, d, n)] + int(input[y_][x_])
        if new_dist < distances[(y_, x_, d_, n_)]:
            distances[(y_, x_, d_, n_)] = new_dist
            heapq.heappush(q, (new_dist, candidate))


print(min([dist for ((y, x, _, n), dist) in distances.items() if y == len(input) - 1 and x == len(input[0]) - 1 and n >= 3]))
