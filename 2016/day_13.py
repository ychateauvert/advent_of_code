#!/usr/bin/env python

from sys import exit
import pdb
from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])
Node = namedtuple("Node", ["distance", "position"])

DESIGNER_FAVORITE_NUMBER = 1352

discovered_locations = {}
visited_locations = {}

def is_wall(position):
    """ Check if a position is a wall
    """
    global discovered_locations
    if position in discovered_locations:
        return discovered_locations[position]

    value = (position.x * position.x) + (3 * position.x) + (2 * position.x * position.y) + position.y + (position.y * position.y) + DESIGNER_FAVORITE_NUMBER

    number_of_ones = "{0:b}".format(value).count("1")
    is_wall = (number_of_ones % 2) == 1

    discovered_locations[position] = is_wall

    return is_wall


def is_valid_position(position):
    if is_wall(position):
        return False

    if position.x < 0 or position.y < 0:
        return False

    if position in visited_locations:
        return False

    return True


def adjacent_node(node):
    new_distance = node.distance + 1
    position = node.position
    positions = []

    positions += [
        Position(position.x + 1, position.y),
        Position(position.x - 1, position.y),
        Position(position.x, position.y + 1),
        Position(position.x, position.y - 1)
    ]

    return [Node(new_distance, position) for position in positions if is_valid_position(position)]


def search_path(destination):
    """ Find shortest path
    """
    global visited_locations

    origin = Node(0, Position(1, 1))
    nodes = adjacent_node(origin)

    visited_locations[origin.position] = True

    while nodes:
        node = nodes.pop(0)

        distance, position = node

        visited_locations[position] = True
        if position.x == destination.x and position.y == destination.y:
            return distance
        else:
            nodes += adjacent_node(node)

def count_path(steps):
    global visited_locations

    origin = Node(0, Position(1, 1))
    visited_locations = {origin.position: True}
    nodes = adjacent_node(origin)

    max_travelled_distance = 0
    i = 0

    while nodes:
        node = nodes.pop(0)

        if node.distance > steps:
            continue

        if node.position not in visited_locations:
            visited_locations[node.position] = True
            nodes += [x for x in adjacent_node(node) if x[0] < steps + 1]

    return len(visited_locations)


def main():
    print('[Part 1] Distance: %s' % search_path(Position(31, 39)))
    print('[Part 2] Number of locations within 50 steps: %s' % count_path(50))

if __name__ == '__main__':
    main()
