#!/usr/bin/env python

import itertools


def valid_password(password):
    """
    >>> valid_password('111111')
    True
    >>> valid_password('223450')
    False
    >>> valid_password('123789')
    False
    """
    has_double = False
    last = None
    for v in password:
        if v == last:
            has_double = True

        if last:
            if int(v) < int(last):
                return False

        last = v

    return has_double


def valid_password_2(password):
    """
    >>> valid_password('112233')
    True
    >>> valid_password('123444')
    False
    >>> valid_password('111122')
    True
    """
    last = None
    for v in password:
        if last:
            if int(v) < int(last):
                return False

        last = v

    result = [len(list(g)) for k, g in itertools.groupby(password)]

    return 2 in result


def part1():
    cnt = 0
    for i in range(152085, 670283):
        if valid_password(str(i)):
            cnt += 1

    return cnt


def part2():
    cnt = 0
    for i in range(152085, 670283):
        if valid_password_2(str(i)):
            cnt += 1

    return cnt


def main():
    # Result: 1764
    print(f"Part 1: {part1()}")
    # Result:
    print(f"Part 2: {part2()}")


if __name__ == '__main__':
    main()