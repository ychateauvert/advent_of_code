#!/usr/bin/env python

import unittest
import challenge

class TestChallenge(unittest.TestCase):

    provided_values = [
        'eedadn',
        'drvtee',
        'eandsr',
        'raavrd',
        'atevrs',
        'tsrnev',
        'sdttsa',
        'rasrtv',
        'nssdts',
        'ntnada',
        'svetve',
        'tesnvt',
        'vntsnd',
        'vrdear',
        'dvrsen',
        'enarar'
    ]

    def test_provided(self):
        self.assertEqual('easter', challenge.part_1(self.provided_values))

    def test_part_2(self):
        self.assertEqual('advent', challenge.part_2(self.provided_values))


if __name__ == '__main__':
    unittest.main()
