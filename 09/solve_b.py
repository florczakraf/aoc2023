import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0

for line in input:
    numbers = [int(x) for x in line.split()]
    levels = [numbers]
    while not all(x == 0 for x in levels[-1]):
        prev = levels[-1][0]
        next_level = []
        for i in levels[-1][1:]:
            next_level.append(i - prev)
            prev = i

        levels.append(next_level)

    carry = 0
    for level in levels[::-1]:
        carry = level[0] - carry
    sum += carry


print(sum)
