import re
import sys



def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

prod = 1
times = [int(x) for x in re.findall(r"\d+", input[0])]
distances = [int(x) for x in re.findall(r"\d+", input[1])]

for time, distance in zip(times, distances):
    n = 0
    for i in range(1, time + 1):
        v = i
        d = v * (time - i)
        if d > distance:
            n += 1
    prod *= n

print(prod)
