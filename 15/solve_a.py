import sys
from pprint import pprint


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

total = 0

def hash(s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

for token in input[0].split(","):
    total += hash(token)

print(total)
