import re

import math
import sys
from collections import defaultdict, Counter
from pathlib import Path
from pprint import pprint
from queue import Queue


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

nodes = set()
edges = defaultdict(set)

for line in input:
    node, neighbors = line.split(": ")
    neighbors = neighbors.split(" ")
    nodes.add(node)
    for neighbor in neighbors:
        nodes.add(neighbor)
        edges[node].add(neighbor)
        edges[neighbor].add(node)


def bfs(start):
    visited = set()
    q = Queue()
    q.put((start, None))
    used_edges = Counter()
    while not q.empty():
        node, prev = q.get()
        if node in visited:
            continue

        if prev is not None:
            used_edges[tuple(sorted((node, prev)))] += 1

        visited.add(node)
        for neighbor in edges[node]:
            if neighbor not in visited:
                q.put((neighbor, node))
    return used_edges, len(visited)

c = Counter()
for node in nodes:
    used_edges, _ = bfs(node)
    c += used_edges

print(c.most_common(3))

for (s, t), _ in c.most_common(3):
    edges[s].remove(t)
    edges[t].remove(s)

_, count = bfs(list(nodes)[0])

print(count * (len(nodes) - count))
