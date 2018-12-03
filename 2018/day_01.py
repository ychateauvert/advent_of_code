#!/usr/bin/env python

from itertools import cycle

value = 0

reached = set()

frequencies = open('inputs/day_01.txt').read().strip().splitlines()
for frequency in frequencies:
    value = value + int(frequency)

print('Day 01 part 1: %s' % value)

value = 0
for frequency in cycle(frequencies):
    value = value + int(frequency)
    if value in reached:
        print('Day 01 part 2: %s' % value)
        exit()
    reached.add(value)
