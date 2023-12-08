import re
import sys
from itertools import cycle


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

steps = cycle(x for x in input[0])
nodes = {}
start = "AAA"
stop = "ZZZ"

for line in input[2:]:
    node, l, r = re.findall(r"[A-Z]{3}", line)
    nodes[node] = (l, r)

n = 0
current = start
while current != stop:
    n += 1
    l, r = nodes[current]
    direction = next(steps)
    if direction == "L":
        current = l
    elif direction == "R":
        current = r

print(n)
