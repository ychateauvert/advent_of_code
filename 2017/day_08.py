#!/usr/bin/env python3

import re
import collections

SPLITTER = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+) ([!<>=]+) (\-?\d+)")
registers = collections.defaultdict(int)

# cpu_instructions = [SPLITTER.match(x).groups() for x in open("tests/day_08.txt").read().strip().splitlines()]
cpu_instructions = [SPLITTER.match(x).groups() for x in open("inputs/day_08.txt").read().strip().splitlines()]


def condition_is_valid(instruction):
    left = registers[instruction[3]]
    right = int(instruction[5])
    operator = instruction[4]

    if operator == "==":
        return left == right
    elif operator == "!=":
        return left != right
    elif operator == "<=":
        return left <= right
    elif operator == ">=":
        return left >= right
    elif operator == ">":
        return left > right
    elif operator == "<":
        return  left < right

    raise "no"


def max_register_value():
    return registers[max(registers, key=lambda i: registers[i])]


def solutions(instructions):
    max_ever_value = 0
    for instruction in instructions:
        if condition_is_valid(instruction):
            if instruction[1] == 'inc':
                registers[instruction[0]] += int(instruction[2])
            else:
                registers[instruction[0]] -= int(instruction[2])
        m = max_register_value()
        if m > max_ever_value:
            max_ever_value = m

    return max_register_value(), max_ever_value


print("Solutions: {}".format(solutions(cpu_instructions)))
