#!/usr/bin/env python

import unittest
import challenge


def test_provided():
    provided = [
        ('ADVENT', 'ADVENT', 6),
        ('A(1x5)BC', 'ABBBBBC', 7),
        ('(3x3)XYZ', 'XYZXYZXYZ', 9),
        ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG', 11),
        ('(6x1)(1x3)A', '(1x3)A', 6),
        ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY', 18),
    ]

    for value, decompressed, length in provided:
        yield check_correct_decompression(value, decompressed, length)

def check_correct_decompression(value, decompressed, length):
    checked = challenge.decompress(value)
    assert length == len(checked)
    # self.assertEqual(length, checked)
    # self.assertEqual(decompressed, checked)



if __name__ == '__main__':
    unittest.main()
