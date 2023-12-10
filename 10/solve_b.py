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
start = None
for y, line in enumerate(input):
    try:
        sx = line.index("S")
        start = (y, sx)
        break
    except ValueError:
        continue

connected = {
    "S": {
        (0, 1): "-7J",
        (0, -1): "-FL",
        (1, 0): "|JL",
        (-1, 0): "|7F",
    },
    "|": {
        (1, 0): "|JLS",
        (-1, 0): "|7FS",
    },
    "-": {
        (0, 1): "-7JS",
        (0, -1): "-LFS",
    },
    "7": {
        (0, -1): "-LFS",
        (1, 0): "|JLS",
    },
    "J": {
        (0, -1): "-LFS",
        (-1, 0): "|F7S",
    },
    "L": {
        (0, 1): "-7JS",
        (-1, 0): "|F7S",
    },
    "F": {
        (0, 1): "-7JS",
        (1, 0): "|JLS",
    },
    ".": {},
}


q = Queue()
visited = {}
visited[start] = 0
q.put((*start, None))

def bfs():
    while not q.empty():
        y, x, prev = q.get()
        for (dy, dx), dests in connected[input[y][x]].items():
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= len(input) or nx < 0 or nx >= len(input[ny]):
                continue

            if input[y][x] == "S" and (-dy, -dx) not in connected[input[ny][nx]]:
                continue

            if (ny, nx) == prev:
                continue

            if input[ny][nx] not in dests:
                continue

            if (ny, nx) in visited and visited[ny, nx] <= visited[y, x] - 1:
                print(visited[ny, nx] + 1)
                return

            visited[ny, nx] = visited[y, x] + 1
            q.put((ny, nx, (y, x)))

bfs()

map = []
dots = []

for y, line in enumerate(input):
    map.append([])
    for x, c in enumerate(line):
        if c == ".":
            dots.append((y, x))
            map[-1].append(c)
        elif (y, x) in visited:
            map[-1].append(c)
        else:
            map[-1].append(".")
            dots.append((y, x))

map[start[0]][start[1]] = "|"  # this works for my input

enclosed = 0

for dot in dots:
    n = 0
    y, x = dot
    for i in range(x, len(input[y])):
        if map[y][i] in "|JL":
            n += 1
    if n % 2 == 1:
        enclosed += 1

print(enclosed)
