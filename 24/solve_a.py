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
hailstone = []


for line in input:
    hailstone.append([int(x) for x in re.findall(r"[-\d]+", line)])


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def intersects(a, b):
    ax, ay, a2x, a2y = a
    bx, by, b2x, b2y = b

    x_diff = ax - a2x, bx - b2x
    y_diff = ay - a2y, by - b2y

    div = det(x_diff, y_diff)
    if div == 0:
        return None, None

    d = det((ax, ay), (a2x, a2y)), det((bx, by), (b2x, b2y))
    x = det(d, x_diff) / div
    y = det(d, y_diff) / div

    return x, y


for i in range(len(hailstone)):
    for j in range(i + 1, len(hailstone)):
        a = (hailstone[i][0], hailstone[i][1], hailstone[i][0] + hailstone[i][3], hailstone[i][1] + hailstone[i][4])
        b = (hailstone[j][0], hailstone[j][1], hailstone[j][0] + hailstone[j][3], hailstone[j][1] + hailstone[j][4])
        x, y = intersects(a, b)
        if x is not None:
            dxa = x - hailstone[i][0]
            dya = y - hailstone[i][1]
            dxb = x - hailstone[j][0]
            dyb = y - hailstone[j][1]

            if not ((dxa > 0) == (hailstone[i][3] > 0) and (dya > 0) == (hailstone[i][4] > 0)) or not ((dxb > 0) == (hailstone[j][3] > 0) and (dyb > 0) == (hailstone[j][4] > 0)):
                continue

            low, high = 7, 27
            low, high = 200000000000000, 400000000000000
            if low <= x <= high and low <= y <= high:
                total += 1


print(total)
