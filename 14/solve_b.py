import sys
from pprint import pprint


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

total = 0

map = []

for line in input:
    map.append(list(line))


def simulate(map):
    for x in range(len(map[0])):
        start = None
        count = 0
        for y in range(len(map)):
            c = map[y][x]
            if c == "#" and start is not None:
                for y_ in range(start, start + count):
                    map[y_][x] = "O"
                for y_ in range(start + count, y):
                    map[y_][x] = "."
                start = None
                count = 0
            elif c == "#":
                start = None
                count = 0
            elif c == "O":
                count += 1
                if start is None:
                    start = y
            elif c == "." and start is None:
                start = y

        if start is not None:
            for y_ in range(start, start+count):
                map[y_][x] = "O"
            for y_ in range(start+count, len(map)):
                map[y_][x] = "."


def rotate(map):
    return [list(x) for x in zip(*map[::-1])]


def step(map):
    for _ in range(4):
        simulate(map)
        map = rotate(map)
    return map


cache = {}
N = 1_000_000_000
for i in range(N):
    map = step(map)
    frozen = str(map)
    if frozen in cache:
        cycle_length = i - cache[frozen]
        if (N - i - 1) % cycle_length == 0:
            break
    cache[frozen] = i

for i, row in enumerate(map[::-1], start=1):
    total += i * row.count("O")

print(total)
