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

workflows = {}
parts = False
total = 0

for line in input:
    if not line:
        parts = True
        continue

    if not parts:
        name, rest = line[:line.index("{")], line[line.index("{")+1:-1]
        workflows[name] = {}
        for part in rest.split(","):
            try:
                condition, target = part.split(":")
            except ValueError:
                condition = "True"
                target = part
            workflows[name][condition] = target
    else:
        orig_context = {}
        for part in line[1:-1].split(","):
            k, v = part.split("=")
            orig_context[k] = int(v)

        context = orig_context.copy()
        workflow = "in"
        while workflow not in ("A", "R"):
            for condition, target in workflows[workflow].items():
                result = eval(condition, context)
                if result:
                    workflow = target
                    break
        if workflow == "A":
            total += sum(orig_context.values())

print(total)
