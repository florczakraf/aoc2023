import re
import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()


seeds = [int(x) for x in input[0].split(": ")[1].split()]
print(f"{seeds=}")

maps = []

for line in input[2:]:
    if not line:
        continue

    if "map" in line:
        maps.append({})
        continue
    current_map = maps[-1]

    numbers = [int(x) for x in re.findall(r"\d+", line)]
    current_map[range(numbers[1], numbers[1] + numbers[2])] = numbers[0] - numbers[1]

locations = []

for seed in seeds:
    value = seed
    for map in maps:
        for r, shift in map.items():
            if value in r:
                # print(f"{value=} {r=} {shift=} {value + shift=}")
                value += shift
                break
    locations.append(value)

print(min(locations))
