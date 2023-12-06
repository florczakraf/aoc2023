import math
import re
import sys



def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

prod = 1
times = [int(x) for x in re.findall(r"\d+", input[0].replace(" ", ""))]
distances = [int(x) for x in re.findall(r"\d+", input[1].replace(" ", ""))]

for time, distance in zip(times, distances):
    min_v = math.ceil((time - math.sqrt(time * time - 4 * distance)) / 2)
    max_v = (time + math.sqrt(time * time - 4 * distance)) // 2

    prod = int(max_v - min_v + 1)

print(prod)
