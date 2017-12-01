#!/usr/bin/env python3

import json

def sum_of_item(item, skip_red=False):

    if isinstance(item, list):
        return sum([sum_of_item(i, skip_red) for i in item])

    if isinstance(item, dict):
        if skip_red and 'red' in item.values():
            return 0
        return sum([sum_of_item(i, skip_red) for i in item.values()])

    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item


def main():
    in_values = "".join([x for x in open("inputs/day_12.txt").read().strip().split("\n")])

    v = json.loads(in_values)

    print("Sum of all numbers: %s", sum_of_item(v))
    print('Correct sum: %s', sum_of_item(v, True))

if __name__ == '__main__':
    main()
