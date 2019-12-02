#!/usr/bin/env python

import math

modules = open('inputs/day_01.txt').read().strip().splitlines()


def calculate_fuel(initial):
    fuel = (math.floor(int(initial) / 3) - 2)
    if fuel < 1:
        return 0

    return fuel + calculate_fuel(fuel)


part1 = 0
part2 = 0

for module in modules:
    part1 = part1 + (math.floor(int(module) / 3) - 2)
    part2 = part2 + calculate_fuel(module)

print('Part 1:')
print(part1)

print('Part 2:')
print(part2)




