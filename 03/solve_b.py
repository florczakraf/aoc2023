import sys
from collections import defaultdict


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0
gears = defaultdict(list)


def has_adjacent_gear(i, j):
    directions_with_diagonals = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]

    for direction in directions_with_diagonals:
        y = i + direction[0]
        x = j + direction[1]

        if y < 0 or y >= len(input):
            continue

        if x < 0 or x >= len(input[y]):
            continue

        c = input[y][x]
        if c == "*":
            return y, x


current_number = 0
gear_position = None

for i, line in enumerate(input):
    if gear_position:
        gears[gear_position].append(current_number)

    current_number = 0
    gear_position = None

    for j, c in enumerate(line):
        if c.isdigit():
            current_number = current_number * 10 + int(c)
            if new_gear_position := has_adjacent_gear(i, j):
                gear_position = new_gear_position
        else:
            if gear_position:
                gears[gear_position].append(current_number)
            current_number = 0
            gear_position = None

if gear_position:
    gears[gear_position].append(current_number)

for gear_position, gear_values in gears.items():
    if len(gear_values) == 2:
        sum += gear_values[0] * gear_values[1]

print(sum)
