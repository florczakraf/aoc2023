import re
import sys
from collections import Counter
from functools import cmp_to_key, cache


def load_stdin():
    return sys.stdin.read().splitlines()

input = load_stdin()

hands = {}

for line in input:
    cards, bet = line.split(" ")
    hands[cards] = int(bet)


@cache
def get_hand_rank(hand):
    counter = Counter(hand)

    j = counter.pop("J", 0)
    try:
        highest, _ = counter.most_common(1)[0]
    except IndexError:
        highest = "J"
    counter[highest] += j

    if len(counter) == 1:
        return 6
    elif len(counter) == 2:
        if 4 in counter.values():
            return 5
        else:
            return 4
    elif len(counter) == 3:
        if 3 in counter.values():
            return 3
        else:
            return 2
    elif len(counter) == 4:
        return 1
    else:
        return 0

CARD_ORDER = "J23456789TQKA"

def compare_equal_hands(hand1, hand2):
    for h1, h2 in zip(hand1, hand2):
        if CARD_ORDER.index(h1) > CARD_ORDER.index(h2):
            return 1
        elif CARD_ORDER.index(h1) < CARD_ORDER.index(h2):
            return -1

def compare_hands(hand1, hand2):
    if get_hand_rank(hand1) > get_hand_rank(hand2):
        return 1
    elif get_hand_rank(hand1) < get_hand_rank(hand2):
        return -1
    else:
        return compare_equal_hands(hand1, hand2)

sorted_hands = sorted(hands.keys(), key=cmp_to_key(compare_hands))


sum = 0
for mul, hand in enumerate(sorted_hands, 1):
    sum += mul * hands[hand]

print(sum)
