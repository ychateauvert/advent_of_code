#!/usr/bin/env python3

import re
import collections

SPLITTER = re.compile(r"(\d+) <-> (.*)")
# input_file = 'tests/day_12.txt'
input_file = 'inputs/day_12.txt'

pipes = [SPLITTER.match(x) for x in open(input_file).read().strip().splitlines()]
programs = set()
pipes_connection = collections.defaultdict(set)

for pipe in pipes:
    pipe_in = int(pipe.group(1))
    pipe_outs = [int(x.strip()) for x in pipe.group(2).split(',')]
    programs.add(pipe_in)
    for p in pipe_outs:
        programs.add(p)
        pipes_connection[p].add(pipe_in)
        pipes_connection[pipe_in].add(p)


def find_all_reachable_to_group(starting_value):
    found_values = set()
    values_to_check = [starting_value]
    while len(values_to_check) > 0:
        to_check = values_to_check.pop()
        for v in pipes_connection[to_check]:
            if v not in found_values:
                found_values.add(v)
                values_to_check.append(v)

    return found_values


def part_1():
    reachable = find_all_reachable_to_group(0)

    return len(reachable)


def part_2():
    group_cnt = 1
    group_1 = find_all_reachable_to_group(0)
    remaining = programs - group_1
    while len(remaining) > 0:
        new_group = find_all_reachable_to_group(remaining.pop())
        group_cnt += 1
        remaining = remaining - new_group

    return group_cnt

print("Part 1: {}".format(part_1()))
print("Part 2: {}".format(part_2()))
