#!/usr/bin/env python

from collections import namedtuple
from itertools import combinations, permutations

Node = namedtuple('Node', ['position', 'size', 'used', 'avail', 'perc_used'])

def is_valid_pair(a, b):
    if a.used == 0:
        return False

    if a.position == b.position:
        return False

    if b.avail - a.used >= 0:
        return True

    return False


def main():
    values = [Node(tuple(map(int, y[0].split('-'))), *map(int, y[1:])) for y in [x.split(' ') for x in open("inputs/day_22.txt").read().strip().split("\n")]]
    nodes = { n.position: n for n in values }

    pairs = [(x, y) for x, y in permutations(values, 2) if is_valid_pair(x, y)]

    print('[Part 1] Valid pairs: %s' % len(pairs))

    max_x = max([x[0] for x in nodes.keys()])


if __name__ == '__main__':
    main()
