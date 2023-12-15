import sys
from collections import deque, defaultdict, OrderedDict
from pprint import pprint


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

total = 0
boxes = defaultdict(dict)
def hash(s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

for token in input[0].split(","):
    if "-" in token:
        label = token[:-1]
        h = hash(label)
        boxes[h].pop(label, None)
    else:
        label, v = token.split("=")
        h = hash(label)
        boxes[h][label] = v


for i in range(256):
    for j, v in enumerate(boxes[i].values(), 1):
        total += (i+1) * j * int(v)

print(total)
