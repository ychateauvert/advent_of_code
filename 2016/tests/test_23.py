#!/usr/bin/env python

import unittest

from day_23 import BunnyAssembler

class TestDay23(unittest.TestCase):

    def test_provided(self):
        provided = [
            "cpy 2 a",
            "tgl a",
            "tgl a",
            "tgl a",
            "cpy 1 a",
            "dec a",
            "dec a",
        ]

        interpreter = BunnyAssembler.load_from_instructions(provided)
        registers = interpreter.interpret()
        self.assertEqual(3, registers['a'])

if __name__ == '__main__':
    unittest.main()
