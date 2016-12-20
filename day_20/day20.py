#!/usr/bin/env python

import sys
import itertools
import pdb

blacklist_rules = itertools.chain.from_iterable([range(int(i[0]), int(i[1]) + 1) for i in [x.split("-") for x in open("input.txt").read().strip().split("\n")]])


def is_blacklisted(value):
    return value not in blacklist_rules


def non_blacklisted(all_values):
    """ Remove all blacklisted values

    >>> remove_blacklisted(range(0, 10), [range(5, 9), range(0, 3), range(4, 8)])
    {3, 9}
    """
    for i in all_values:
        if i not in blacklist_rules:
            print('Found %s' % i)
            yield(i)


def main():
    global blacklist_rules

    values = range(0, 4294967295)

    # for valid in non_blacklisted(values):
        # print('[Part 1] Found %s' % valid)
        # sys.exit(0)

    print("[Part 2] Valid ips: %s" % len(list(non_blacklisted(values))))


if __name__ == '__main__':
    main()
