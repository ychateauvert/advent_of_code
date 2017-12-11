#!/usr/bin/env python3

import collections

child_direction = open('inputs/day_11.txt').read().strip().split(',')

# Thanks to this resource: https://www.redblobgames.com/grids/hexagons/


def find_distance(directions):
    """
    :param directions:
    :return:
    >>> find_distance(['ne', 'ne', 'ne'])
    3
    >>> find_distance(['ne', 'ne', 'sw', 'sw'])
    0
    >>> find_distance(['ne', 'ne', 's', 's'])
    2
    >>> find_distance(['se', 'sw', 'se', 'sw', 'sw'])
    3
    """
    x = 0
    y = 0
    z = 0

    how_far = []
    for direction in directions:
        if direction == "n":
            y += 1
            z -= 1
        elif direction == "s":
            y -= 1
            z += 1
        elif direction == "ne":
            x += 1
            z -= 1
        elif direction == "sw":
            x -= 1
            z += 1
        elif direction == "nw":
            x -= 1
            y += 1
        elif direction == "se":
            x += 1
            y -= 1
        how_far.append((abs(x) + abs(y) + abs(z)) / 2)

    return ((abs(x) + abs(y) + abs(z)) / 2, max(how_far))


# import doctest
# doctest.testmod()

part_1, part_2 = find_distance(child_direction)
print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))
