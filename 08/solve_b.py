import math
import re
import sys
from itertools import cycle


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

steps = cycle(x for x in input[0])
nodes = {}
starts = []
stops = []

for line in input[2:]:
    node, l, r = (re.findall(r"[A-Z0-9]{3}", line))

    if node.endswith("A"):
        starts.append(node)

    nodes[node] = (l, r)

ns = []
for start in starts:
    n = 0
    current = start
    while not current.endswith("Z"):
        n += 1
        l, r = nodes[current]
        direction = next(steps)
        if direction == "L":
            current = l
        elif direction == "R":
            current = r

    ns.append(n)

answer = ns[0]
for n in ns[1:]:
    answer = answer * n // math.gcd(answer, n)

print(answer)
