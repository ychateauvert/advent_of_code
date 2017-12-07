#!/usr/bin/env python3

import re
import collections

STACKED_ON = re.compile(r"(\w+) \(\d+\) -> (.*)")
DISC_WEIGHT = re.compile(r"(\w+) \((\d+)\)")


def balancing_discs(definition):
    balancing = dict()
    for line in definition:
        m = STACKED_ON.match(line)
        if m:
            balancing[m.group(1)] = [x.strip() for x in m.group(2).split(',')]

    return balancing


def part_1(definition):
    was_stacked = set()
    for line in definition:
        m = STACKED_ON.match(line)
        if m:
            for disc in [x.strip() for x in m.group(2).split(',')]:
                was_stacked.add(disc)

    for disc, weight in discs:
        if disc not in was_stacked:
            return disc


def weight_calculation(node):
    if node not in discs_to_balance:
        return weights[node]

    return weights[node] + sum([weight_calculation(c) for c in discs_to_balance[node]])


def misbehaving_program(node):
    children = discs_to_balance[node]
    if not children:
        return node
    ws = [(x, weight_calculation(x)) for x in children]
    by_w = collections.defaultdict(list)
    for disc, w in ws:
        by_w[w].append(disc)

    odd_one = False
    normal = False
    for k, v in by_w.items():
        if len(v) == 1:
            odd_one = k
        if len(v) > 1:
            normal = k

    if not odd_one:
        return False

    for disc, w in ws:
        if w == odd_one:
            p = misbehaving_program(disc)
            if not p:
                ww = weights[disc]
                # Put breakpoint here. check difference between odd_one and normal
                # then result will be the delta applied to ww
                return disc
            return p

    raise "doh"


def part_2(root_node):
    # children = discs_to_balance[root_node]
    # w = [(x, weight_calculation(x)) for x in children]
    p = misbehaving_program(root_node)


puzzle_definition = open("inputs/day_07.txt").read().strip().splitlines()
# puzzle_definition = open("tests/day_07.txt").read().strip().splitlines()
discs = [DISC_WEIGHT.match(x).groups() for x in puzzle_definition]

weights = {disc: int(w) for disc, w in discs}
discs_to_balance = balancing_discs(puzzle_definition)

root = part_1(puzzle_definition)
print("Part 1: {}".format(root))
# print("Part 2: {}".format(part_2(root)))
part_2(root)

# Part 2 resolved in debugger
