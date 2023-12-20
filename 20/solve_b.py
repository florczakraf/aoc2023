import math
import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from pprint import pprint
from queue import Queue


def load_stdin():
    # return Path("input").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

target_map = {}
flip_flop_state = {}
conjunction_state = {}

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


rx_source = [s for s, targets in target_map.items() if "rx" in targets][0]
rx_sources = [s for s, targets in target_map.items() if rx_source in targets]


def count_cycles():
    q = Queue()

    for i in range(1, 100000):
        q.put(("broadcaster", False, None))
        while not q.empty():
            name, v, prev = q.get()
            if name in rx_sources and not v:
                yield i

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

cycles_iterator = count_cycles()
cycles = []
for i in range(len(rx_sources)):
    cycles.append(next(cycles_iterator))

lcm = cycles[0]
for n in cycles[1:]:
    lcm = lcm * n // math.gcd(lcm, n)

print(lcm)
