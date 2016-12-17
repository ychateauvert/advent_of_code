#!/usr/bin/env python

import re

PUZZLE_INPUT = '01111001100111011'

R_DOUBLE = re.compile(r"([0-1]{1})\1")


def chunks(data, n):
    """ Split into chunks

    >>> list(chunks("110010110100", 2))
    ['11', '00', '10', '11', '01', '00']
    """
    for i in range(0, len(data), n):
        yield "".join(data[i:i + n])

def flip_value(value):
    if value == '0':
        return '1'
    return '0'

def fill_disk(current_data, size):
    """ Fill disk to requested size

    >>> fill_disk("1", 3)
    '100'

    >>> fill_disk("11111", len("11111000000"))
    '11111000000'

    >>> fill_disk("111100001010", 25)
    '1111000010100101011110000'
    """
    while len(current_data) <= size:
        a = current_data
        b = "".join([flip_value(x) for x in reversed(current_data)])

        current_data = a + "0" + b
    return current_data[:size]


def zero_or_one(value):
    """ Return 0 or 1 dependending on the value

    >>> zero_or_one("00")
    '1'

    >>> zero_or_one("11")
    '1'

    >>> zero_or_one("01")
    '0'

    >>> zero_or_one("10")
    '0'
    """
    if R_DOUBLE.match(value):
        return '1'

    return '0'


def checksum_value(data):
    """ Checksum the data

    >>> checksum_value("110010110100")
    '100'
    """
    checksum = "".join([zero_or_one(x) for x in chunks(data, 2)])

    if len(checksum) % 2:
        return checksum

    return checksum_value(checksum)


def fill_and_checksum(current_data, length):
    disk = fill_disk(current_data, length)
    return checksum_value(disk)


def main():
    print("[Part 1] Checksum %s" % fill_and_checksum(PUZZLE_INPUT, 272))
    print("[Part 2] Checksum %s" % fill_and_checksum(PUZZLE_INPUT, 35651584))


if __name__ == '__main__':
    main()
