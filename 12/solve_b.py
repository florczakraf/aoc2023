import re
import sys
from functools import cache


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

total = 0

@cache
def count_arrangements(springs: str, numbers: tuple[int]):
    if not numbers:
        if springs.count("#") == 0:
            return 1
        else:
            return 0

    if sum(numbers) > len(springs):
        return 0

    if springs[0] == ".":
        return count_arrangements(springs[1:], numbers)

    without_spring = 0
    with_spring = 0

    if springs[0] == "?":
        without_spring = count_arrangements(springs[1:], numbers)

    possible_spring = all(c in "?#" for c in springs[:numbers[0]])
    possible_end = len(springs) == numbers[0] or springs[numbers[0]] in ".?"

    if possible_spring and possible_end:
        with_spring = count_arrangements(springs[numbers[0] + 1:], numbers[1:])

    return without_spring + with_spring


for line in input:
    springs, numbers = line.split()
    numbers = [int(x) for x in numbers.split(",")] * 5
    springs = "?".join([springs for x in range(5)])

    total += count_arrangements(springs, tuple(numbers))


print(total)
