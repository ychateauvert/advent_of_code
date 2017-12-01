#!/usr/bin/env python

from collections import defaultdict

from day_23 import BunnyAssembler

def main():
    interpreter = BunnyAssembler.load_script('inputs/day_12.txt')
    registers = interpreter.interpret()
    print("[Part 1] Value in 'a' register: %s" % registers['a'])

    registers = interpreter.interpret({"c": 1})
    print("[Part 2] Value in 'a' when register 'c' is initialized: %s" % registers['a'])


if __name__ == '__main__':
    main()
