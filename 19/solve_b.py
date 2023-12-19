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
total = 0

for line in input:
    if not line:
        break

    name, rest = line[:line.index("{")], line[line.index("{")+1:-1]
    workflows[name] = {}
    for part in rest.split(","):
        try:
            condition, target = part.split(":")
        except ValueError:
            condition = "True"
            target = part
        workflows[name][condition] = target

q = Queue()
q.put({"workflow": "in", "x0": 1, "x1": 4000, "m0": 1, "m1": 4000, "a0": 1, "a1": 4000, "s0": 1, "s1": 4000})
while not q.empty():
    context = q.get()
    workflow = context["workflow"]
    if workflow == "A":
        value = 1
        for c in "xmas":
            value *= 1 + context[c + "1"] - context[c + "0"]
        total += value
        continue
    elif workflow == "R":
        continue

    for condition, target in workflows[workflow].items():
        if condition == "True":
            q.put({**context, "workflow": target})
        else:
            c = condition[0]
            op = condition[1]
            v = int(condition[2:])

            new_context = {**context, "workflow": target}
            if op == "<":
                new_context[c + "1"] = min(new_context[c + "1"], v - 1)
                q.put(new_context)
                context[c + "0"] = max(context[c + "0"], new_context[c + "1"] + 1)
            elif op == ">":
                new_context[c + "0"] = max(new_context[c + "0"], v + 1)
                q.put(new_context)
                context[c + "1"] = min(context[c + "1"], new_context[c + "0"] - 1)

print(total)
