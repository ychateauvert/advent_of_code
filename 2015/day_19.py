#!/usr/bin/env python3

import re
import collections
from random import sample

medicine_molecule = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

CONVERTER = re.compile(r"(\w+) => (\w+)")
RULES = re.compile(r"(Al|B|Ca|F|H|Mg|N|O|P|Si|Th|Ti|e)")

puzzle = [CONVERTER.match(x).groups() for x in open('inputs/day_19.txt').read().strip().split("\n")]

# medicine_molecule = 'HOH'
# medicine_molecule = 'HOHOHO'
# puzzle = [
#     ('e', 'H'),
#     ('e', 'O'),
#     ('H', 'HO'),
#     ('H', 'OH'),
#     ('O', 'HH')
# ]

replacements = {r: l for l, r in puzzle}


# def all_possible_replacements(molecule):
#     possible_molecule = set()
#     for m in RULES.finditer(molecule):
#         orig = m.group()
#         for r in rules[orig]:
#             possible_molecule.add(molecule[:m.start()] + r + molecule[m.end():])
#
#     return possible_molecule


def find_min_steps(medicine):
    steps = 0
    final = medicine
    while final != 'e':
        temp = final
        for n in sample(list(replacements), len(replacements)):
            if n in final:
                steps += final.count(n)
                final = final.replace(n, replacements[n])

        if final == temp:
            final = medicine
            steps = 0
            continue

    return steps

# print("Part 1: {}".format(len(all_possible_replacements(medicine_molecule))))
print("Part 2: {}".format(find_min_steps(medicine_molecule)))
