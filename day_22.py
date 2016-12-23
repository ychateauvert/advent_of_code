#!/usr/bin/env python

from collections import namedtuple

Node = namedtuple('Node', ['position', 'size', 'used', 'avail', 'perc_used'])

def main():
    values = [Node(tuple(y[0].split('-')), *y[1:]) for y in [x.split(' ') for x in open("inputs/day_22.txt").read().strip().split("\n")]]


if __name__ == '__main__':
    main()
