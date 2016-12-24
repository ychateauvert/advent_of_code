#!/usr/bin/env python

import unittest

from day_23 import AssembunnyInterpreter

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

        interpreter = AssembunnyInterpreter.load_from_instructions(provided)
        self.assertEqual(3, interpreter.interpret()["a"])

if __name__ == '__main__':
    unittest.main()
