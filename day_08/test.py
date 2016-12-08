#!/usr/bin/env python

import unittest

from challenge import Panel

class TestChallenge(unittest.TestCase):

    def test_provided_swipe(self):
        instructions = [
            "rect 3x2",
            "rotate column x=1 by 1",
            "rotate row y=0 by 4",
            "rotate column x=1 by 1"
        ]
        panel = Panel(7, 3)
        panel.swipe(instructions)
        self.assertEqual([
                ".#..#.#",
                "#.#....",
                ".#....."
            ],
            panel.display()
        )
        panel.lit_pixels()

    def test_provided_manual(self):

        panel = Panel(7, 3)
        self.assertEqual(
            [".......",
            ".......",
            "......."],
            panel.display()
        )

        panel.rect(3, 2)
        self.assertEqual([
                "###....",
                "###....",
                "......."
            ],
            panel.display(),
            "Rect"
        )

        panel.rotate_column(1, 1)
        self.assertEqual([
                "#.#....",
                "###....",
                ".#....."
            ],
            panel.display(),
            "Rotate Column 1:1"
        )

        panel.rotate_row(0, 4)
        self.assertEqual([
                "....#.#",
                "###....",
                ".#....."
            ],
            panel.display(),
            "Rotate Row 0:4"
        )

        panel.rotate_column(1, 1)
        self.assertEqual([
                ".#..#.#",
                "#.#....",
                ".#....."
            ],
            panel.display(),
            "Rotate Column 1:1"
        )

    def test_lit_pixels(self):
        panel = Panel(7, 3)
        self.assertEqual(0, panel.lit_pixels())


    def test_row(self):
        panel = Panel(10, 5)


if __name__ == '__main__':
    unittest.main()
