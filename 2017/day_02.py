#!/usr/bin/env python3

import itertools


spreadsheet = [list(map(int, x.split())) for x in open("inputs/day_02.txt").read().strip().split("\n")]

part_1 = sum(max(x) - min(x) for x in spreadsheet)

print("Part 1: {}".format(part_1))

part_2 = 0
for row in spreadsheet:
    for i, j in itertools.combinations(row, 2):
        vals = [i, j]
        if max(vals) % min(vals) == 0:
            part_2 += max(vals) / min(vals)
            break

print(part_2)
