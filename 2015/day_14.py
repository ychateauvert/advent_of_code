#!/usr/bin/env python3

import re
from collections import namedtuple

PUZZLE_PARSING = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds")

RacePos = namedtuple(
    'RacePos',
    ['distance', 'sprinting_time', 'resting_time']
)
Participant = namedtuple(
    'Participant',
    ['name', 'speed', 'sprint_time', 'resting_time']
)


class Position:
    def __init__(self, participant):
        self.participant = participant
        self.points = 0

    def name(self):
        return self.participant.name

    def distance(self, ticks):
        cycle_time = self.participant.sprint_time + self.participant.resting_time
        cycles, remain = divmod(ticks, cycle_time)
        dist = cycles * self.participant.speed * self.participant.sprint_time
        if remain > self.participant.sprint_time:
            dist += self.participant.speed * self.participant.sprint_time
        else:
            dist += remain * self.participant.speed
        return dist

    def from_specification(spec):
        return Position(
            Participant(
                spec[0],
                int(spec[1]),
                int(spec[2]),
                int(spec[3])
            )
        )


def find_winner_at(participants, no_of_ticks):
    """
    :param participants:
    :param no_of_ticks:
    :return:

    >>> find_winner_at([("Comet", 14, 10, 127), ("Dancer", 16, 11, 162)], 1000)
    'Comet'
    """
    race = [Position.from_specification(x) for x in participants]
    position = sorted([(x.name(), x.distance(no_of_ticks)) for x in race], key=lambda p: p[1], reverse=True)
    print(position)
    winner, *loser = position
    return winner


def main():
    # import doctest
    # doctest.testmod()
    puzzle = [PUZZLE_PARSING.match(x).groups() for x in open('inputs/day_14.txt').read().strip().split("\n")]
    winner = find_winner_at(puzzle, 2503)
    print(winner)

    # Part 2:
    racers = [Position.from_specification(x) for x in puzzle]

    for i in range(1, 2503):
        dists = sorted([(r, r.distance(i)) for r in racers], key=lambda x: x[1], reverse=True)
        dists[0][0].points = dists[0][0].points + 1

    winner, *losers = sorted(racers, key=lambda x: x.points, reverse=True)
    print(winner.name(), winner.points)

if __name__ == '__main__':
    main()
