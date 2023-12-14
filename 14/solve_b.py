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
    for _ in range(len(map) - 1):
        for y in range(1, len(map)):
            for x in range(len(map[0])):
                if map[y][x] == "O" and map[y - 1][x] == ".":
                    map[y][x] = "."
                    map[y - 1][x] = "O"

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
