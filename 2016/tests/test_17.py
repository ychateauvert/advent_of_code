#!/usr/bin/env python

import day_17
import unittest


class TestDay17(unittest.TestCase):

    def test_adjacent_rooms(self):
        start_node = day_17.Node(day_17.Tile(0, 0), 'hijkl', '')
        valid_nodes = start_node.adjacents()
        self.assertEqual(1, len(valid_nodes))

    def test_provided(self):
        shortest, longest = day_17.shortest_path('ihgpwlah')
        self.assertEqual('DDRRRD', shortest)
        self.assertEqual(370, len(longest))

        shortest, longest = day_17.shortest_path('kglvqrro')
        self.assertEqual('DDUDRLRRUDRD', shortest)
        self.assertEqual(492, len(longest))

        shortest, longest = day_17.shortest_path('ulqzkmiv')
        self.assertEqual('DRURDRUDDLLDLUURRDULRLDUUDDDRR', shortest)
        self.assertEqual(830, len(longest))


if __name__ == '__main__':
    unittest.main()
