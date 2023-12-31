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

for _ in range(len(map) - 1):
    for y in range(1, len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "O" and map[y - 1][x] == ".":
                map[y][x] = "."
                map[y - 1][x] = "O"

for i, row in enumerate(map[::-1], start=1):
    total += i * row.count("O")

print(total)
