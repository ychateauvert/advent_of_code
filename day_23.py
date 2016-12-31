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
        self.toggled = dict()

        self.current_instruction = 0
        try:
            while True:
                instruction, *args = self.instructions[self.current_instruction]

                if self.current_instruction in self.toggled:
                    # print("Toggled %s, %s" % (instruction, args))
                    self.current_instruction += self.inversed(instruction, args)
                else:
                    # print("Regular %s, %s" % (instruction, args))
                    self.current_instruction += self.regular(instruction, args)

                # print(self.registers)
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

        return 1

    def load_script(filename):
        return BunnyAssembler.load_from_instructions(open(filename).read().strip().split("\n"))

    def load_from_instructions(instructions):
        instructions = [x.split(" ") for x in instructions]
        return BunnyAssembler(instructions)


def main():
    interpreter = BunnyAssembler.load_script('inputs/day_23.txt')
    registers = interpreter.interpret({"a": 7})
    print("[Part 1] Value in 'a' register: %s" % registers['a'])

    registers = interpreter.interpret({"a": 12})
    print("[Part 2] Value in 'a' register: %s" % registers['a'])

if __name__ == '__main__':
    main()
