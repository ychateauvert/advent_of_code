#!/usr/bin/env python

import pdb

from collections import namedtuple, defaultdict
from itertools import combinations, groupby

from copy import deepcopy

provided_test_data = [
    [('M', 'H'), ('M', 'L')],
    [('G', 'H')],
    [('G', 'L')],
    []
]

part_1_data = [
    [('G', 'S'), ('M', 'S'), ('G', 'P'), ('M', 'P')],
    [('G', 'T'), ('G', 'R'), ('M', 'R'), ('G', 'C'), ('M', 'C')],
    [('M', 'T')],
    []
]

test_equivalent = [
    [
        [('G', 'H')],
        [('M', 'H')],
        [('G', 'L'), ('M', 'L')],
        []
    ],
    [
        [('G', 'L')],
        [('M', 'L')],
        [('M', 'H'), ('G', 'H')],
        []
    ]
]

HASH_KEY_LENGTH = 5

Node = namedtuple("Node", ["floor", "distance", "puzzle"])

visited = {
    0: set(),
    1: set(),
    2: set(),
    3: set()
}

def equivalent(a, b):
    """ Are puzzle equivalent (for pruning)

    >>> equivalent(*map(serialize_puzzle, test_equivalent))
    True
    """
    if len(a) != len(b):
        return False

    for c_a, c_b in zip(a, b):
        if c_a in ['G', 'M'] and c_a != c_b:
            return False

    return True


def has_equivalent(node):
    return any([x for x in visited[node.floor] if equivalent(node.puzzle, x)])


def serialize_puzzle(puzzle):
    """ Serialize puzzle for hash map

    >>> serialize_puzzle(provided_test_data)
    'MHML GH GL'
    """
    return " ".join(["".join(sorted([''.join(y) for y in x])) for x in puzzle]).rstrip()


def visit(node):
    global visited
    serialized = serialize_puzzle(node.puzzle)
    visited[node.floor].add(serialized)


def is_visited(node):
    serialized = serialize_puzzle(node.puzzle)

    return serialized in visited[node.floor]


def pruned(adjacent_nodes):
    adjacents = [n for n in adjacent_nodes if not is_visited(n) and not has_equivalent(n)]

    return adjacents


def lower_levels_empty(floor, puzzle):
    return sum(map(len, puzzle[:floor])) == 0


def available_floors(floor, puzzle):
    if lower_levels_empty(floor, puzzle):
        return [floor + 1]

    return [floor for floor in [floor - 1, floor + 1] if floor >= 0 and floor < len(puzzle)]


def find_complement(item):
    kind, material = item

    if kind == 'M':
        return ('G', material)

    return ('M', material)


def win_condition(puzzle):
    return

def is_valid(node):
    for row in node.puzzle:
        if len(row) != 0:
            # for k, v in groupby(row, lambda x: x[0]):
                # print(k)
                # # print(list(v))
                # if k == 'G':
                    # print("nope")
                    # generators = list(v)
                # elif k == 'M':
                    # print('yes')
                    # microchips == list(v)
                    # print(microchips)
                    # print('yes2')

            # print(row)
            # print(generators)
            # print(microchips)
            # print('-----------------')
            # generators = [x for x in row if x[0] == 'G']

            if len(generators) == 0:
                continue

            # microchips = [x for x in row if x[0] == 'M']

            if len(set(microchips) - set(generators)) == 0:
                continue

    return True


def clone_puzzle(puzzle):
    return [x[:] for x in puzzle]


def adjacent_nodes(node):
    nodes = []
    new_distance = node.distance + 1
    floors = available_floors(node.floor, node.puzzle)

    for floor in floors:
        for item in node.puzzle[node.floor]:
            puzzle = clone_puzzle(node.puzzle)
            puzzle[node.floor].remove(item)

            puzzle[floor].append(item)
            nodes.append(Node(floor, new_distance, puzzle))

        for a, b in combinations(node.puzzle[node.floor], 2):
            puzzle = clone_puzzle(node.puzzle)
            puzzle[node.floor].remove(a)
            puzzle[node.floor].remove(b)

            puzzle[floor].append(a)
            puzzle[floor].append(b)

            nodes.append(Node(floor, new_distance, puzzle))

    return pruned([node for node in nodes if is_valid(node)])


def search(puzzle):
    origin = Node(0, 0, puzzle)
    nodes = adjacent_nodes(origin)

    while nodes:
        node = nodes.pop(0)

        visit(node)
        if len(node.puzzle[0]) == len(node.puzzle[1]) == len(node.puzzle[2]) == 0:
            return node.distance
        else:
            nodes += adjacent_nodes(node)


def main():
    # result = search(part_1_data)
    result = search(provided_test_data)

    print("[Part 1] Shortest distance %s" % result)


if __name__ == '__main__':
    main()
