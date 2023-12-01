import re
import sys


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

sum = 0

digits_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
}

for line in input:
    print(line)
    digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    print(digits)
    sum += int("".join((digits_map[digits[0]], digits_map[digits[-1]])))

print(sum)
