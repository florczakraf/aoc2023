import re
import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0

for line in input:
    digits = re.findall(r"\d", line)
    sum += int("".join((digits[0], digits[-1])))

print(sum)
