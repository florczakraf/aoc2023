import re
import sys
from collections import defaultdict
from queue import Queue


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

cards = defaultdict(lambda: 0)

to_process = Queue()

for line in input:
    numbers = re.findall(r"\d+|\|", line)
    print(numbers)
    pipe = numbers.index("|")
    card_id = int(numbers[0])
    winning = {int(x) for x in numbers[1:pipe]}
    card = {int(x) for x in numbers[pipe+1:]}

    common = len(winning.intersection(card))
    cards[card_id] += 1
    if common:
        for i in range(card_id + 1, card_id + common + 1):
            cards[i] += cards[card_id]


print(sum(cards.values()))
