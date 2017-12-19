#!/usr/bin/env python3

import re

SPIN = re.compile(r'^s(\d+)')
EXCHANGE = re.compile(r'^x(\d+)/(\d+)')
PARTNER = re.compile(r'^p(\w+)/(\w+)')

dance = open("inputs/day_16.txt").read().strip().split(',')


def apply_instruction(programs, instruction):
    """
    :param programs:
    :param instruction:
    :return:
    >>> apply_instruction("abcde", "s1")
    'eabcd'
    >>> apply_instruction("eabcd", "x3/4")
    'eabdc'
    >>> apply_instruction("eabdc", "pe/b")
    'baedc'
    """
    new_programs = list(programs[:])
    if SPIN.match(instruction):
        i = int(SPIN.match(instruction).group(1))
        new_programs = programs[-i:] + programs[:-i]
    elif EXCHANGE.match(instruction):
        from_idx, to_idx = EXCHANGE.match(instruction).groups()
        new_programs[int(from_idx)] = programs[int(to_idx)]
        new_programs[int(to_idx)] = programs[int(from_idx)]
    elif PARTNER.match(instruction):
        from_c, to_c = PARTNER.match(instruction).groups()
        from_idx = programs.index(from_c)
        to_idx = programs.index(to_c)
        new_programs[int(from_idx)] = programs[int(to_idx)]
        new_programs[int(to_idx)] = programs[int(from_idx)]

    return "".join(new_programs)


def part_1(programs):
    for dance_move in dance:
        programs = apply_instruction(programs, dance_move)

    return programs


def part_2(programs):
    seen = []
    for i in range(1000000000):
        s = programs[:]
        if s in seen:
            # Since we're cycling, the first cycle we find we can know the end state
            return seen[1000000000 % i]
        seen.append(s)

        for dance_move in dance:
            programs = apply_instruction(programs, dance_move)


initial_programs = "abcdefghijklmnop"
print(part_1(initial_programs))

print(part_2(initial_programs))

# import doctest
# doctest.testmod()
