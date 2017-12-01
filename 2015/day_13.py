#!/usr/bin/env python3

import re
import itertools
import collections

R_HAPPY = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)')


def main():
    puzzle_input = [x for x in open("inputs/day_13.txt").read().strip().split("\n")]
    chart = collections.defaultdict(lambda: 0)
    guests = []
    for seating in puzzle_input:
        (p1, direction, happiness, p2) = R_HAPPY.match(seating).groups()
        if direction == 'gain':
            direction = 1
        else:
            direction = -1

        chart[(p1, p2)] = int(happiness) * direction

        guests.append(p1)
        guests.append(p2)

    guests = set(guests)
    possible_seatings = list(itertools.permutations(guests))

    print('Max happiness: {}'.format(max([calculate_happiness(chart, x) for x in possible_seatings])))

    guests.add('ygreenc')
    possible_seatings = list(itertools.permutations(guests))
    print('Max happiness with me: {}'.format(max([calculate_happiness(chart, x) for x in possible_seatings])))


def calculate_happiness(chart, seating):
    seating = list(seating)
    right = zip(seating, seating[1:] + [seating[0]])
    left = zip(reversed(seating), list(reversed(seating))[1:] + [seating[-1]])

    return sum([chart[x] for x in right]) + sum([chart[x] for x in left])


if __name__ == '__main__':
    main()
