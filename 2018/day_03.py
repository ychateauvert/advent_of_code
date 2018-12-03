#!/usr/bin/env python

import re
import numpy as np

R_RULE = re.compile(r"^\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


def print_fabric(f):
    for row in f:
        for col in row:
            if col == 0:
                print('.', end='')
            else:
                print(col, end='')
        print()


rules = list(map(lambda r: R_RULE.match(r), open('inputs/day_03.txt').read().strip().splitlines()))

fabric = np.full((1000, 1000), 0)
claims = np.full((1000, 1000), 0)

valid_claims = set(map(lambda r: int(r.group(1)), rules))
invalid_claims = set()

for rule in rules:
    claim_id, x, y, w, h = rule.groups()
    for i in range(int(h)):
        for j in range(int(w)):
            fabric[int(y)+i][int(x)+j] += 1
            if claims[int(y)+i][int(x)+j] != 0:
                invalid_claims.add(int(claim_id))
                invalid_claims.add(int(claims[int(y)+i][int(x)+j]))

            claims[int(y)+i][int(x)+j] = int(claim_id)

part1 = 0
for row in fabric:
    part1 += len(list(filter((lambda x: x > 1), row)))

print('Day 03 part 1: %s' % part1)

part2 = valid_claims - invalid_claims
print('Day 03 part 2: %s' % part2)
