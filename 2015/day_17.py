#!/usr/bin/env python3

import itertools

demo_containers = [20, 15, 10, 5, 5]

puzzle_containers = [
    50,
    44,
    11,
    49,
    42,
    46,
    18,
    32,
    26,
    40,
    21,
    7,
    18,
    43,
    10,
    47,
    36,
    24,
    22,
    40
]

def possible_buckets(containers, quantity):
    for i in range(len(containers), 0, -1):
        c = itertools.combinations(containers, i)
        for i in c:
            if sum(i) == quantity:
                yield i


# demo = possible_buckets(demo_containers, 25)

real = list(possible_buckets(puzzle_containers, 150))
print('Part 1: {}'.format(len(real)))

min_amount = min([len(i) for i in real])
possibles = [x for x in real if len(x) == min_amount]
print('Part 2: {}'.format(len(possibles)))

