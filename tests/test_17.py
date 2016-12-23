#!/usr/bin/env python

import day17
import unittest


class TestDay17(unittest.TestCase):

    def test_adjacent_rooms(self):
        start_node = day17.Node(day17.Tile(0, 0), 'hijkl', '')
        valid_nodes = start_node.adjacents()
        self.assertEqual(1, len(valid_nodes))

    def test_provided(self):
        self.assertEqual('DDRRRD', day17.shortest_path('ihgpwlah'))
        self.assertEqual('DDUDRLRRUDRD', day17.shortest_path('kglvqrro'))
        self.assertEqual('DRURDRUDDLLDLUURRDULRLDUUDDDRR', day17.shortest_path('ulqzkmiv'))


if __name__ == '__main__':
    unittest.main()
