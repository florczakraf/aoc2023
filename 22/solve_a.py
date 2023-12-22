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
bricks = []


for line in input:
    brick = [int(x) for x in re.findall(r"\d+", line)]
    bricks.append(brick)

bricks = sorted(bricks, key=lambda x: x[2])

def drop_brick(brick, heights):
    z = max(heights[x, y] for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1))
    diff = max(brick[2] - z - 1, 0)

    return [brick[0], brick[1], brick[2] - diff, brick[3], brick[4], brick[5] - diff]

def simulate(bricks):
    dropped = False
    heights = defaultdict(lambda: 0)
    next_bricks = []

    for brick in bricks:
        new_brick = drop_brick(brick, heights)
        if brick != new_brick:
            dropped = True
        next_bricks.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                heights[x, y] = new_brick[5]

    return dropped, next_bricks

_, fallen_bricks = simulate(bricks)

for i in range(len(fallen_bricks)):
    dropped, _ = simulate(fallen_bricks[:i] + fallen_bricks[i + 1:])
    if not dropped:
        total += 1

print(total)
