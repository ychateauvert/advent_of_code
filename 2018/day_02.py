#!/usr/bin/env python

from collections import Counter
from itertools import permutations

aoc = open('inputs/day_02.txt').read().strip().splitlines()
challenge_input = map((lambda x: Counter(x)), aoc)

twice = 0
thrice = 0


def only_1_diff(str1, str2):
    found = False
    for a, b in zip(str1, str2):
        if a != b and found:
            return False
        elif a != b:
            found = True

    return found


def find_correct_pair():
    for str1, str2 in permutations(aoc, 2):
        if only_1_diff(str1, str2):
            return str1, str2


for boxId in challenge_input:
    double = [l for l, c in boxId.most_common() if c == 2]
    triple = [l for l, c in boxId.most_common() if c == 3]

    if double:
        twice += 1

    if triple:
        thrice += 1

part1 = twice * thrice
print('Day 02 part 1: %s' % part1)

str1, str2 = find_correct_pair()
common = [x for x, y in zip(str1, str2) if x == y]

part2 = ''.join(common)
print('Day 02 part 2: %s' % part2)

