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

    if maxes["red"] <= 12 and maxes["green"] <= 13 and maxes["blue"] <= 14:
        _, game_id = game.split(" ")
        sum += int(game_id)

print(sum)
