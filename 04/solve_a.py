import re
import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0

for line in input:
    numbers = re.findall(r"\d+|\|", line)
    print(numbers)
    pipe = numbers.index("|")
    winning = {int(x) for x in numbers[1:pipe]}
    card = {int(x) for x in numbers[pipe+1:]}

    print(f"{winning=}")
    print(f"{card=}")

    common = len(winning.intersection(card))
    if common:
        print(numbers[0], ":", 1 << (common - 1))
        sum += 1 << (common - 1)

print(sum)
