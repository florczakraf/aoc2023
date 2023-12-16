import sys
from pprint import pprint


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

visited = set()
start = (0, 0, "r")
visited.add(start)
stack = [start]


def generate(y, x, d):
    c = input[y][x]
    if d == "r":
        if c in (".", "-"):
            return [(y, x+1, "r")]
        elif c == "/":
            return [(y-1, x, "u")]
        elif c == "\\":
            return [(y+1, x, "d")]
        elif c == "|":
            return [(y-1, x, "u"), (y+1, x, "d")]
    elif d == "d":
        if c in (".", "|"):
            return [(y+1, x, "d")]
        elif c == "/":
            return [(y, x-1, "l")]
        elif c == "\\":
            return [(y, x+1, "r")]
        elif c == "-":
            return [(y, x-1, "l"), (y, x+1, "r")]
    elif d == "l":
        if c in (".", "-"):
            return [(y, x-1, "l")]
        elif c == "/":
            return [(y+1, x, "d")]
        elif c == "\\":
            return [(y-1, x, "u")]
        elif c == "|":
            return [(y-1, x, "u"), (y+1, x, "d")]
    elif d == "u":
        if c in (".", "|"):
            return [(y-1, x, "u")]
        elif c == "/":
            return [(y, x+1, "r")]
        elif c == "\\":
            return [(y, x-1, "l")]
        elif c == "-":
            return [(y, x-1, "l"), (y, x+1, "r")]


while stack:
    y, x, d = stack.pop()
    visited.add((y, x, d))
    candidates = generate(y, x, d)
    for c in candidates:
        y_, x_, _ = c
        if y_ < 0 or y_ >= len(input) or x_ < 0 or x_ >= len(input[0]):
            continue

        if c not in visited:
            stack.append(c)

print(len({(y, x) for y, x, _ in visited}))
