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

target_map = {}
flip_flop_state = {}
conjunction_state = {}
q = Queue()

for line in input:
    if line.startswith("broadcaster"):
        name, targets = line.split(" -> ")
        target_map[name] = targets.split(", ")
    elif line.startswith("%"):
        name, targets = line.split(" -> ")
        target_map[name[1:]] = targets.split(", ")
        flip_flop_state[name[1:]] = False
    elif line.startswith("&"):
        name, targets = line.split(" -> ")
        target_map[name[1:]] = targets.split(", ")
        conjunction_state[name[1:]] = {}

for f in flip_flop_state.keys():
    for t in target_map[f]:
        if t in conjunction_state:
            conjunction_state[t][f] = False


sums = {False: 0, True: 0}
for _ in range(1000):
    q.put(("broadcaster", False, None))
    while not q.empty():
        name, v, prev = q.get()
        sums[v] += 1

        if name in flip_flop_state:
            if not v:
                flip_flop_state[name] = not flip_flop_state[name]
                for t in target_map.get(name, []):
                    q.put((t, flip_flop_state[name], name))
        elif name in conjunction_state:
            conjunction_state[name][prev] = v
            state = not all(conjunction_state[name].values())
            for t in target_map.get(name, []):
                q.put((t, state, name))
        else:
            for t in target_map.get(name, []):
                q.put((t, v, name))


print(sums[True] * sums[False])
