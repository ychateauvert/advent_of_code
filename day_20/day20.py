#!/usr/bin/env python

import sys
from itertools.chain import from_iterable
import pdb

blacklist_rules = [range(int(i[0]), int(i[1]) + 1) for i in [x.split("-") for x in open("input.txt").read().strip().split("\n")]]


def is_blacklisted(value):
    for rule in blacklist_rules:
        if value in rule:
            return True

    return False


def non_blacklisted(all_values):
    """ Remove all blacklisted values

    >>> remove_blacklisted(range(0, 10), [range(5, 9), range(0, 3), range(4, 8)])
    {3, 9}
    """
    for i in all_values:
        if not is_blacklisted(i):
            yield(i)


def main():
    global blacklist_rules

    values = range(0, 4294967295)

    blacklist_rules = [range(int(i[0]), int(i[1]) + 1) for i in [x.split("-") for x in open("input.txt").read().strip().split("\n")]]
    # for valid in non_blacklisted(values):
        # print('[Part 1] Found %s' % valid)
        # sys.exit(0)

    print("[Part 2] Valid ips: %s" % len(list(non_blacklisted(values))))


if __name__ == '__main__':
    main()
