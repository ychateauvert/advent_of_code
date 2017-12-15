#!/usr/bin/env python3

import itertools

firewall = [list(map(int, x.split(': '))) for x in open('inputs/day_13.txt').read().strip().splitlines()]
# firewall = [[0, 3], [1, 2], [4, 4], [6, 4]]

depths = {i: j for i, j in firewall}


def severity(delay=0):
    total = 0
    for layer, depth in firewall:
        if (layer + (delay + 1)) % ((depth - 1) * 2) == 0:
            total += layer * depth

    return total


def part_1():
    return severity()


def part_2():
    for wait in itertools.count():
        if not any(scanner_position(depths[pos], wait + pos) == 0 for pos in depths):
            return wait


def scanner_position(depth, time):
    offset = time % ((depth - 1) * 2)

    return 2 * (depth - 1) - offset if offset > depth - 1 else offset

print("Part 1: {}".format(severity()))

# Severity 0 !== not caught
print("Part 2: {}".format(part_2()))

