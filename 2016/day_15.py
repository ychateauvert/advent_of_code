#!/usr/bin/env python

import re
from itertools import count

R_DISC = re.compile(r"Disc #(\d+) has (\d+).*time=(\d+).*\W(\d+)\.$")

class Disc:
    def __init__(self, index, positions, starting_position):
        self.index = int(index)
        self.positions = int(positions)
        self.starting_position = int(starting_position)

    def is_open(self, time):
        real_time = time + self.index
        position = real_time + self.starting_position

        return (position % self.positions) == 0

    def load(raw):
        return Disc(*R_DISC.match(raw).group(1, 2, 4))

    def __str__(self):
        return "[%s] Positions: %s, Starting position %s" % (self.index, self.positions, self.starting_position)


def find_when_all_opened(values):
    for time in count():
        if all([x.is_open(time) for x in values]):
            return time


def main():
    provided = [
        Disc(1, 5, 4),
        Disc(2, 2, 1)
    ]

    in_values = [Disc.load(x) for x in open("inputs/day_15.txt").read().strip().split("\n")]

    print("[Part 1] You should press the button at time %s" % find_when_all_opened(in_values))
    last_disc = Disc(7, 11, 0)
    print("[Part 2] You should press the button at time %s" % find_when_all_opened(in_values + [last_disc]))



if __name__ == '__main__':
    main()
