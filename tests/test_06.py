#!/usr/bin/env python

import unittest
import day_06

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
        self.assertEqual('easter', day_06.part_1(self.provided_values))

    def test_part_2(self):
        self.assertEqual('advent', day_06.part_2(self.provided_values))
