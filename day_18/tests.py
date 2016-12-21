#!/usr/bin/env python

import unittest

import day18

class TestDay18(unittest.TestCase):

    def test_provided_simple(self):
        floor = day18.map_floor('.^^.^.^^^^', 10)

        self.assertEqual(10, len(floor))
        self.assertEqual(38, day18.safe_tiles(floor))

    def test_next_row(self):
        self.assertEqual('.^^^^', day18.next_row('..^^.'))
        self.assertEqual('^^..^', day18.next_row('.^^^^'))


if __name__ == '__main__':
    unittest.main()
