import sys


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()
galaxies = []
xs = set()
ys = set()
for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((y, x))
            xs.add(x)
            ys.add(y)

double_rows = set(range(len(input))) - ys
double_columns = set(range(len(input[0]))) - xs


sum = 0
for i in range(len(galaxies) - 1):
    y0, x0 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        y1, x1 = galaxies[j]

        y_min, y_max = sorted([y0, y1])
        x_min, x_max = sorted([x0, x1])

        d_rows = set(range(y_min, y_max + 1)) & double_rows
        d_columns = set(range(x_min, x_max + 1)) & double_columns

        distance = abs(y0 - y1) + abs(x0 - x1) + len(d_rows) * (1000000-1) + len(d_columns) * (1000000-1)

        sum += distance

print(sum)
