import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0

for line in input:
    maxes = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }

    game, draws = line.split(": ")
    draws_batches = draws.split("; ")

    for draw_batch in draws_batches:
        draws = draw_batch.split(", ")
        for draw in draws:
            n, color = draw.split(" ")
            maxes[color] = max(maxes[color], int(n))

    sum += maxes["red"] * maxes["green"] * maxes["blue"]

print(sum)
