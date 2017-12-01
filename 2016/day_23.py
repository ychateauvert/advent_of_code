#!/usr/bin/env python

import sys
import pdb

from collections import defaultdict


class BunnyAssembler:
    def __init__(self, instructions):
        self.registers = dict()
        self.toggled = dict()
        self.current_instruction = 0
        self.instructions = instructions

        self.max_prints = -1

    def read(self, register):
        try:
            return int(register)
        except:
            return self.registers[register]

    def interpret(self, registers=None):
        if not registers:
            registers = defaultdict(int)

        self.registers = registers

        self.current_instruction = 0
        try:
            while True:
                instruction, *args = self.instructions[self.current_instruction]

                if self.current_instruction in self.toggled:
                    self.current_instruction += self.inversed(instruction, args)
                else:
                    self.current_instruction += self.regular(instruction, args)
        except IndexError:
            pass

        return self.registers

    def inversed(self, instruction, args):
        if len(args) == 1:
            if instruction == 'inc':
                self.registers[args[0]] -= 1
            else:
                self.registers[args[0]] += 1
        elif len(args) == 2:
            if instruction == 'jnz':
                value, register = args
                self.registers[register] = self.read(value)
            else:
                register, offset = args
                if self.read(register) != 0:
                    return self.read(offset)
        return 1

    def regular(self, instruction, args):
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
                return self.read(offset)
        elif instruction == 'tgl':
            offset = self.registers[args[0]]
            self.toggled[offset + self.current_instruction] = True
        elif instruction == 'out':
            register = args[0]
            print(self.read(register))
            if self.max_prints != -1:
                self.max_prints -= 1
                if self.max_prints == 0:
                    sys.exit(0)

        return 1

    @staticmethod
    def load_script(filename):
        return BunnyAssembler.load_from_instructions(open(filename).read().strip().split("\n"))

    @staticmethod
    def load_from_instructions(instructions):
        instructions = [x.split(" ") for x in instructions]
        return BunnyAssembler(instructions)


def main():
    if not sys.stdin.isatty():
        input_stream = sys.stdin.read().strip().split("\n")
        interpreter = BunnyAssembler.load_from_instructions(input_stream)
        if len(sys.argv) == 2:
            interpreter.max_prints = int(sys.argv[1])
        interpreter.interpret()
    else:
        interpreter = BunnyAssembler.load_script('inputs/day_23.txt')
        registers = interpreter.interpret({"a": 7})

        print("[Part 1] Value in 'a' register: %s" % registers['a'])

        registers = interpreter.interpret({"a": 12})
        print("[Part 2] Value in 'a' register: %s" % registers['a'])

if __name__ == '__main__':
    main()
