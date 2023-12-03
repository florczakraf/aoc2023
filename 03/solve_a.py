import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0


def has_adjacent_symbol(i, j):
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
        if not c.isdigit() and c != ".":
            return True

    return False


current_number = 0
has_symbol = False

for i, line in enumerate(input):
    if current_number > 0 and has_symbol:
        sum += current_number

    current_number = 0
    has_symbol = False

    for j, c in enumerate(line):
        if c.isdigit():
            current_number = current_number * 10 + int(c)
            if has_adjacent_symbol(i, j):
                has_symbol = True
        else:
            if has_symbol:
                sum += current_number
            current_number = 0
            has_symbol = False

if has_symbol:
    sum += current_number

print(sum)
