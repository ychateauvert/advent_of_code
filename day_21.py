#!/usr/bin/env python

import pdb
import re

R_MOVE = re.compile(r"move position (\d+) to position (\d+)")
R_SWAP_POS = re.compile(r"swap position (\d+) with position (\d)")
R_SWAP_LET = re.compile(r"swap letter (\w+) with letter (\w+)")
R_REVERSE = re.compile(r"reverse positions (\d+) through (\d+)")
R_ROTATE_DIR = re.compile(r"rotate (\w+) (\d+) step")
R_ROTATE_POS = re.compile(r"rotate based on position of letter (\w+)")

def move_position(start, end):
    """ Remove start and insert at end

    >>> move_position(1, 4)('bcdea')
    'bdeac'

    >>> move_position(2, 6)('abcdefgh')
    'abdefgch'

    >>> move_position(1, 4)('bdeac', True)
    'bcdea'
    """
    def perform(value, reverse=False):
        fro, to = start, end
        if reverse:
            fro, to = to, fro

        value = list(value)
        a = value.pop(fro)

        v = value[:to] + [a] + value[to:]
        return "".join(v)

    return perform


def swap_position(start, end):
    """ Swap 2 characters position

    >>> swap_position(4, 0)('abcde')
    'ebcda'

    >>> swap_position(4, 0)('ebcda', True)
    'abcde'
    """
    def perform(value, reverse=False):
        value = list(value)
        a = value[start]
        value[start] = value[end]
        value[end] = a

        return "".join(value)

    return perform


def swap_letters(a, b):
    """ Swap 2 letters

    >>> swap_letters('d', 'b')('ebcda')
    'edcba'

    >>> swap_letters('d', 'b')('edcba', True)
    'ebcda'
    """
    def perform(value, reverse=False):
        value = value.replace(b, '#')
        value = value.replace(a, b)
        value = value.replace('#', a)

        return value

    return perform


def rotate_direction(direction, steps):
    """ Rotate in direction -1 means right

    >>> rotate_direction(1, 1)('abcde')
    'bcdea'

    >>> rotate_direction(-1, 2)('bcdea')
    'eabcd'

    >>> rotate_direction(-1, 6)('ecabd')
    'decab'

    >>> rotate_direction(-1, 6)('decab', True)
    'ecabd'

    >>> rotate_direction(-1, 2)('eabcd', True)
    'bcdea'
    """
    def perform(value, reverse=False):
        multiplier = direction
        if reverse:
            multiplier *= -1
        cutoff = (multiplier * steps) % len(value)

        return value[cutoff:] + value[:cutoff]

    return perform


def rotate_position(letter):
    """ Rotate string by index of first occurrence

    >>> rotate_position('b')('abdec')
    'ecabd'

    >>> rotate_position('d')('ecabd')
    'decab'

    >>> rotate_position('d')('decab', True)
    'ecabd'

    >>> rotate_position('b')('ecabd', True)
    'abdec'
    """
    def perform(value, reverse=False):
        if not reverse:
            first_occ = value.find(letter)
            if first_occ >= 4:
                first_occ += 1

            return rotate_direction(-1, first_occ + 1)(value)
        else:
            unscrambled = value
            rotate_left = rotate_direction(1, 1)
            rotator = rotate_position(letter)
            while True:
                unscrambled = rotate_left(unscrambled)

                if rotator(unscrambled) == value:
                    return unscrambled

    return perform


def reverse_position(start, end):
    """ Reverse substring

    >>> reverse_position(0, 4)('edcba')
    'abcde'

    >>> reverse_position(0, 4)('abcde', True)
    'edcba'
    """
    def perform(value, reverse=False):
        return value[:start] + "".join(reversed(value[start:end + 1])) + value[end + 1:]

    return perform


def scramble_rule(rule):
    if R_MOVE.match(rule):
        m = R_MOVE.match(rule)
        return move_position(int(m.group(1)), int(m.group(2)))
    elif R_REVERSE.match(rule):
        m = R_REVERSE.match(rule)
        return reverse_position(int(m.group(1)), int(m.group(2)))
    elif R_SWAP_LET.match(rule):
        m = R_SWAP_LET.match(rule)
        return swap_letters(m.group(1), m.group(2))
    elif R_SWAP_POS.match(rule):
        m = R_SWAP_POS.match(rule)
        return swap_position(int(m.group(1)), int(m.group(2)))
    elif R_ROTATE_DIR.match(rule):
        m = R_ROTATE_DIR.match(rule)
        if m.group(1) == 'right':
            direction = -1
        else:
            direction = 1

        return rotate_direction(direction, int(m.group(2)))
    elif R_ROTATE_POS.match(rule):
        m = R_ROTATE_POS.match(rule)
        return rotate_position(m.group(1))


def main():
    instructions = [x for x in open("inputs/day_21.txt").read().strip().split("\n")]
    scramble = list(map(scramble_rule, instructions))

    password = 'abcdefgh'

    for r in scramble:
        password = r(password)

    print("[Part 1] Scrambled password: %s" % password)

    password = 'fbgdceah'
    for r in reversed(scramble):
        password = r(password, True)

    print("[Part 2] Unscrambled password fbgdceah == %s" % password)


if __name__ == '__main__':
    main()
