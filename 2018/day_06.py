#!/usr/bin/env python

from collections import Counter


def grid_limits(coordinates):
    """
    :param coordinates:
    :return:
    >>> grid_limits([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    (1, 8, 1, 9)
    """
    min_x = min(map(lambda x: x[0], coordinates))
    max_x = max(map(lambda x: x[0], coordinates))
    min_y = min(map(lambda x: x[1], coordinates))
    max_y = max(map(lambda x: x[1], coordinates))

    return min_x, max_x, min_y, max_y


def manhattan_distance(a, b):
    """

    :param a:
    :param b:
    :return:
    >>> manhattan_distance((5, 1), (1, 1))
    4
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def closest_coordinate(location, coordinates):
    """

    :param location:
    :param coordinates:
    :return:
    >>> closest_coordinate((5, 1), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    False
    >>> closest_coordinate((4, 1), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    (1, 1)
    >>> closest_coordinate((5, 2), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    (5, 5)
    """
    is_double = False
    min_value = False
    min_coord = False
    for coordinate in coordinates:
        distance = manhattan_distance(coordinate, location)
        if min_value == distance and distance is not False:
            is_double = True
        elif min_value > distance or not min_value:
            is_double = False
            min_coord = coordinate
            min_value = distance

    if is_double:
        return False

    return min_coord


def is_finite(location, coordinates):
    """
    :param location:
    :param coordinates:
    :return:
    >>> is_finite((1, 1), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    False
    >>> is_finite((1, 6), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    False
    >>> is_finite((8, 3), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    False
    >>> is_finite((5, 5), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    True
    >>> is_finite((3, 4), [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    True
    """
    min_x, max_x, min_y, max_y = grid_limits(coordinates)
    x, y = location

    return min_x < x < max_x and min_y < y < max_y


def area_shortest_shared_distance(coordinates):
    """

    :param coordinates:
    :return:
    >>> area_shortest_shared_distance([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
    17
    """
    closest_locations = dict()
    min_x, max_x, min_y, max_y = grid_limits(coordinates)
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if (x, y) in coordinates:
                closest_locations[(x, y)] = (x, y)
            else:
                closest_locations[x, y] = closest_coordinate((x, y), coordinates)

    areas = Counter(closest_locations.values())

    for location, count in areas.most_common():
        if is_finite(location, coordinates):
            return count

    exit('Broken')


if __name__ == '__main__':
    coordinates = list(map(lambda x: tuple(map(int, x.split(', '))), open('inputs/day_06.txt').read().strip().splitlines()))
    part1 = area_shortest_shared_distance(coordinates)

    print('Day 06 part 1: %s' % part1)
