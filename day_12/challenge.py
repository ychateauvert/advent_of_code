#!/usr/bin/env python

import re
import sys
import pdb

from collections import defaultdict

provided_values = [
    "cpy 41 a",
    "inc a",
    "inc a",
    "dec a",
    "jnz a 2",
    "dec a"
]

registers = defaultdict(int)

def read(register):
    try:
        return int(register)
    except:
        return registers[register]

def execute_bunnyassem(instructions):
    """ Execute Bunny Assembler instructions

    >>> execute_bunnyassem(provided_values)['a']
    42
    """
    current_instruction = 0
    try:
        while True:
            instruction = instructions[current_instruction]
            if instruction.startswith('cpy'):
                value, register = re.match(r"cpy (\w+) (\w+)", instruction).groups([1, 2])
                registers[register] = read(value)
            elif instruction.startswith('inc'):
                register = re.match(r"inc ([a-z]{1})", instruction).group(1)
                registers[register] += 1
            elif instruction.startswith('dec'):
                register = re.match(r"dec ([a-z]{1})", instruction).group(1)
                registers[register] -= 1

            if instruction.startswith('jnz'):
                register, offset = re.match(r"jnz (\w+) ([-]?\d+)", instruction).groups([1, 2])
                if read(register) != 0:
                    current_instruction += int(offset)
                    continue

            current_instruction += 1

    except IndexError:
        # Stop executing when trying to access out of array element
        pass

    return registers


def main():
    global registers
    data = open("input.txt").read().split("\n")
    execute_bunnyassem(data)
    print("[Part 1] Value in 'a' register: %s" % registers['a'])

    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    execute_bunnyassem(data)
    print("[Part 2] Value in 'a' when register 'c' is initialized: %s" % registers['a'])


if __name__ == '__main__':
    main()
