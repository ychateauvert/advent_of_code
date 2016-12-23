#!/usr/bin/python

import re
import sys
from io import StringIO

provided_part_1 = [
    ('ADVENT', 'ADVENT'),
    ('A(1x5)BC', 'ABBBBBC'),
    ('(3x3)XYZ', 'XYZXYZXYZ'),
    ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
    ('(6x1)(1x3)A', '(1x3)A'),
    ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY'),
]

provided_part_2 = [
    ('(3x3)XYZ', 'XYZXYZXYZ'),
    ('X(8x2)(3x3)ABCY', 'XABCABCABCABCABCABCY'),
]

R_MATCHER = re.compile(r"\((\d+)x(\d+)\)")

def part_1(value):
    """Decompress special easter bunny file

    >>> all([expected == part_1(x) for x, expected in provided_part_1])
    True

    >>> part_1('ADVENT')
    'ADVENT'

    >>> part_1('A(1x5)BC')
    'ABBBBBC'

    >>> part_1('X(8x2)(3x3)ABCY')
    'X(3x3)ABC(3x3)ABCY'

    >>> part_1('X(8x2)(3x3)ABCY')
    'X(3x3)ABC(3x3)ABCY'
    """
    stream = StringIO(value)
    in_parenthese = None
    result = ""
    while True:
        c = stream.read(1)
        if not c:
            return result

        if in_parenthese:
            in_parenthese += c
            if c == ')':
                length, times = R_MATCHER.match(in_parenthese).groups([1, 2])
                repeatable = stream.read(int(length))
                result += repeatable * int(times)
                in_parenthese = None
        elif c == '(':
            in_parenthese = '('
        else:
            result += c


def split_paren(value):
    return R_MATCHER.match(in_parenthese).groups([1, 2])


def expand_parentheses(stream, length, times):
    pattern = stream.read(length)

def decompress(value):
    while value:
        match = R_MATCHER.search(value)

        if match is None:
            yield len(value) # Abort when no more parenthesis pair
            break

        yield len(value[:match.start()]) # Count until parenthesis
        value = value[match.end():] # Strip the parenthesis
        length, times = match.groups([1, 2])
        length = int(length)
        times = int(times)
        multiply_me = value[:length]
        value =  value[length:]

        for count in decompress(multiply_me):
            yield count * times # Count the sub-pattern (and multiply according to previous factor)


def main():
    original = open("inputs/day_09.txt").read().strip('\n')
    decompressed = part_1(original)

    print("[Part 1] Length of the file: Compressed=%s, Decompressed=%s" % (len(original), len(decompressed)))
    print("[Part 2] Length of the file recursive: %s" % sum(decompress(original)))


if __name__ == '__main__':
    main()
