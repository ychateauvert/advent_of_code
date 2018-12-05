#!/usr/bin/env python

import string

to_remove = [
    ''.join(x)
    for x
    in list(zip(string.ascii_lowercase, string.ascii_uppercase)) + list(zip(string.ascii_uppercase, string.ascii_lowercase))
]


def reduce_polymer(polymer):
    """
    :param polymer:
    :return:

    >>> reduce_polymer('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    """
    while True:
        found_pair = False
        for pair in to_remove:
            if pair in polymer:
                found_pair = True
                polymer = ''.join(polymer.split(pair))

        if not found_pair:
            return polymer


def part_2(polymer):
    """
    :param polymer:
    :return:
    >>> part_2('dabAcCaCBAcCcaDA')
    4
    """
    cleaned_up = []
    for letter in string.ascii_lowercase:
        p = polymer.replace(letter, '')
        p = p.replace(letter.upper(), '')

        cleaned_up.append(p)

    reduced = [reduce_polymer(x) for x in cleaned_up]

    return min(map(len, reduced))


if __name__ == "__main__":
    suit_polymer = open('inputs/day_05.txt').read().strip()
    part1 = reduce_polymer(suit_polymer)
    print('Day 05 part 1: %s' % len(part1))

    part2 = part_2(suit_polymer)
    print('Day 05 part 2: %s' % part2)

