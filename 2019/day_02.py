#!/usr/bin/env python

raw_puzzle = open('inputs/day_02.txt').read().strip()
puzzle_input = [int(x) for x in raw_puzzle.split(',')]


def s_to_m(memory_str):
    return [int(x) for x in memory_str.split(',')]


def m_to_s(memory):
    return ",".join([str(x) for x in memory])


def add(memory, address):
    _, x, y, output = memory[address:address+4]
    memory[output] = memory[x] + memory[y]

    return address + 4


def multiply(memory, address):
    _, x, y, output = memory[address:address+4]
    memory[output] = memory[x] * memory[y]

    return address + 4


def abort(memory, address):
    return False


opcodes = {
    1: add,
    2: multiply,
    99: abort
}


def run_instruction(memory, position=0):
    if memory[position] == 99:
        return False
    opcode, first_val, second_val, output = memory[position:position+4]
    if opcode == 1:
        memory[output] = memory[first_val] + memory[second_val]
    elif opcode == 2:
        memory[output] = memory[first_val] * memory[second_val]

    return True


def run_program(memory, position=0):
    """
    >>> current_execution(s_to_m('1,0,0,0,99'))[0]
    2
    >>> current_execution(s_to_m('2,3,0,3,99'))[0]
    2
    >>> current_execution(s_to_m('2,4,4,5,99,0'))[0]
    2
    >>> current_execution(s_to_m('1,1,1,4,99,5,6,0,99'))[0]
    30
    """
    current_execution = memory.copy()
    while run_instruction(current_execution, position):
        position += 4

    return current_execution


def part1(memory):
    memory = memory.copy()
    memory[1], memory[2] = 12, 2

    return run_program(memory)[0]


def part2(memory):
    for i in range(100):
        for j in range(100):
            part2_memory = memory.copy()
            part2_memory[1], part2_memory[2] = i, j

            if run_program(part2_memory)[0] == 19690720:
                return 100 * i + j


def main():
    # Result: 2692315
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")


if __name__ == '__main__':
    main()


def test_part1(puzzle):
    """
    >>> test_part1('1,0,0,0,99')
    '2,0,0,0,99'
    >>> test_part1('2,3,0,3,99')
    '2,3,0,6,99'
    >>> test_part1('2,4,4,5,99,0')
    '2,4,4,5,99,9801'
    """
    program = [int(x) for x in puzzle.split(',')]
    run_program(program)
    return ",".join([str(x) for x in program])
