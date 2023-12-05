import math
import re
import sys
from pprint import pprint


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

seeds_ranges = [int(x) for x in input[0].split(": ")[1].split()]
ranges = [range(seeds_ranges[start], seeds_ranges[start] + seeds_ranges[start + 1]) for start in range(0, len(seeds_ranges), 2)]

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


min_location = math.inf
seeds = []

for map in maps[::-1]:
    new_extra_seeds = set()
    for seed in seeds:
        for r, shift in map.items():
            if seed in range(r.start + shift, r.stop + shift + 1):
                new_extra_seeds.add(seed - shift)

        new_extra_seeds.add(seed)

    for r, shift in map.items():
        new_extra_seeds.add(r.start)
        new_extra_seeds.add(r.stop)

    seeds = sorted(new_extra_seeds)

seeds = {x for x in seeds if any(x in r for r in ranges)}

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
