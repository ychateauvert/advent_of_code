#!/usr/bin/env python

import unittest

import pdb

from day_24 import HVAC

provided = [
    '###########',
    '#0.1.....2#',
    '#.#######.#',
    '#4.......3#',
    '###########'
]

class TestDay24(unittest.TestCase):

    def test_provided(self):
        system = HVAC(provided)
        self.assertEqual(14, system.visit_all_fewest())

    # def test_shortest_path(self):
        # hvac = HVAC.from_list(provided)

        # self.assertEqual(2, hvac.shortest_path(0, 4))
        # self.assertEqual(2, hvac.shortest_path(0, 1))
        # self.assertEqual(4, hvac.shortest_path(4, 1))
        # self.assertEqual(6, hvac.shortest_path(1, 2))
        # self.assertEqual(2, hvac.shortest_path(2, 3))

    # def test_adjacent_nodes(self):
        # hvac = HVAC(provided)

        # self.assertEqual([(1, 2), (2, 1)], hvac.adjacent_nodes((1, 1)))
        # self.assertEqual([(4, 1), (6, 1)], hvac.adjacent_nodes((5, 1)))
        # self.assertEqual([(8, 1), (9, 2)], hvac.adjacent_nodes((9, 1)))



if __name__ == '__main__':
    unittest.main()
