#!/usr/bin/env python

from collections import defaultdict

class Tile:
    def __init__(self, tile):
        self.tile = tile

    def is_safe(self):
        return self.tile == '.'

    def is_trap(self):
        return self.tile == '^'


class Row:
    def __init__(self, row):
        self.row = row

    def __getitem__(self, key):
        if key < 0 or key >= len(self.row):
            return Tile('.')

        return Tile(self.row[key])

    def __repr__(self):
        return self.row


def next_row(row):
    r = Row(row)
    new_row = ["."] * len(row)
    for i, tile in enumerate(row):
        left, center, right = r[i - 1], r[i], r[i + 1]

        # Rule 1:
        if left.is_trap() and center.is_trap() and right.is_safe():
            new_row[i] = '^'

        # Rule 2:
        if left.is_safe() and center.is_trap() and right.is_trap():
            new_row[i] = '^'

        # Rule 3:
        if left.is_trap() and center.is_safe() and right.is_safe():
            new_row[i] = '^'

        # Rule 4:
        if left.is_safe() and center.is_safe() and right.is_trap():
            new_row[i] = '^'

    return "".join(new_row)



def map_floor(starting_row, requested_rows):
    floor = [starting_row]
    while len(floor) < requested_rows:
        floor.append(next_row(floor[-1]))

    return floor


def safe_tiles(floor):
    return sum([row.count('.') for row in floor])


def main():
    starting_row = open("inputs/day_18.txt").read().strip()

    print("[Part 1] Safe tiles in 40 rows: %s" % safe_tiles(map_floor(starting_row, 40)))
    print("[Part 2] Safe tiles in 400000: %s" % safe_tiles(map_floor(starting_row, 400000)))


if __name__ == '__main__':
    main()

