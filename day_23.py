#!/usr/bin/env python

from collections import defaultdict

class BunnyAssembler:
    def __init__(self, instructions):
        self.instructions = instructions

    def read(self, register):
        try:
            return int(register)
        except:
            return self.registers[register]

    def interpret(self, registers=None):
        if not registers:
            registers = defaultdict(int)

        self.registers = registers

        current_instruction = 0
        try:
            while True:
                instruction, *args = self.instructions[current_instruction]
                if instruction == 'cpy':
                    value, register = args
                    self.registers[register] = self.read(value)
                elif instruction == 'inc':
                    self.registers[args[0]] += 1
                elif instruction == 'dec':
                    self.registers[args[0]] -= 1
                elif instruction == 'jnz':
                    register, offset = args
                    if self.read(register) != 0:
                        current_instruction += int(offset)
                        continue

                current_instruction += 1
        except IndexError:
            pass

        return self.registers

    def load_script(filename):
        return BunnyAssembler.load_from_instructions(open(filename).read().strip().split("\n"))

    def load_from_instructions(instructions):
        instructions = [x.split(" ") for x in instructions]
        return BunnyAssembler(instructions)


def main():
    interpreter = BunnyAssembler.load_script('inputs/day_12.txt')
    registers = interpreter.interpret()
    print("[Part 1] Value in 'a' register: %s" % registers['a'])

    registers = interpreter.interpret({"c": 1})
    print("[Part 2] Value in 'a' when register 'c' is initialized: %s" % registers['a'])


if __name__ == '__main__':
    main()
