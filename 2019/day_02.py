#!/usr/bin/env python

import sys

original_memory = [int(x) for x in open('inputs/day_02.txt').read().strip().split(',')]


def run_instruction(memory, position):
    if memory[position] == 99:
        return False
    opcode, first_val, second_val, output = memory[position:position+4]
    if opcode == 1:
        memory[output] = memory[first_val] + memory[second_val]
    elif opcode == 2:
        memory[output] = memory[first_val] * memory[second_val]

    return True


def run_program(memory, position=0):
    while run_instruction(memory, position):
        position += 4


def part1_run_program(opcodes):
    """
    >>> part1_run_program('1,0,0,0,99')
    '2,0,0,0,99'
    >>> part1_run_program('2,3,0,3,99')
    '2,3,0,6,99'
    >>> part1_run_program('2,4,4,5,99,0')
    '2,4,4,5,99,9801'
    """
    program = [int(x) for x in opcodes.split(',')]
    run_program(program)
    return ",".join([str(x) for x in program])


part1_memory = original_memory.copy()
part1_memory[1], part1_memory[2] = 12, 2
run_program(part1_memory)
print(f"Part 1: {part1_memory[0]}")
# Result: 2692315

for i in range(100):
    for j in range(100):
        part2_memory = original_memory.copy()
        part2_memory[1], part2_memory[2] = i, j

        run_program(part2_memory)

        if part2_memory[0] == 19690720:
            print(f"Part 2: {100 * i + j}")
            sys.exit()
