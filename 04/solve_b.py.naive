import re
import sys
from queue import Queue


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

cards = {}

to_process = Queue()

for line in input:
    numbers = re.findall(r"\d+|\|", line)
    print(numbers)
    pipe = numbers.index("|")
    card_id = int(numbers[0])
    winning = {int(x) for x in numbers[1:pipe]}
    card = {int(x) for x in numbers[pipe+1:]}

    common = len(winning.intersection(card))
    cards[card_id] = common

    to_process.put(card_id)


sum = 0
while not to_process.empty():
    sum += 1
    card_id = to_process.get()
    common = cards[card_id]
    if common:
        for i in range(card_id + 1, card_id + common + 1):
            to_process.put(i)

print(sum)
