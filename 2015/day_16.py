#!/usr/bin/env python3

import re

valid_keys = [
    'children',
    'cats',
    'samoyeds',
    'pomeranians',
    'akitas',
    'vizlas',
    'goldfish',
    'trees',
    'cars',
    'perfumes'
]

real_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

greather_than = ['cats', 'trees']
less_than = ['pomeranians', 'goldfish']


def matching_components(components):
    for k, v in components.items():
        kk = k.lstrip()
        if real_sue[kk] != v:
            return False

    return True


def matching_components_part2(components):
    for k, v in components.items():
        kk = k.lstrip()
        if kk in greather_than:
            if real_sue[kk] >= v:
                return False
        elif kk in less_than:
            if real_sue[kk] <= v:
                return False
        elif real_sue[kk] != v:
            return False

    return True

splitter = re.compile(r"Sue (\d+): (.+)")

puzzle = [splitter.match(x).groups() for x in open("inputs/day_16.txt").read().strip().split("\n")]
possible_sues = []
possible_sues_part_2 = []
for (aunt, characteristics) in puzzle:
    comps = [tuple(x.split(': ')) for x in characteristics.split(',')]
    comps = dict([(x, int(y)) for x, y in comps])
    if matching_components(comps):
        possible_sues.append(aunt)
    if matching_components_part2(comps):
        possible_sues_part_2.append(aunt)

print(possible_sues)
print(possible_sues_part_2)
