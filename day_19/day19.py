#!/usr/bin/env python

from itertools import cycle

CHALLENGE_INPUT = 3014603


def find_white_elephant_winner(participants_count):
    """ Find who won the white elephant game. Index starts at 1

    >>> find_white_elephant_winner(5)
    3
    """
    participants = range(1, participants_count + 1)
    gifts_distribution = [(i, 1) for i in participants]

    while len(gifts_distribution) > 1:
        stealer, gifts = gifts_distribution.pop(0)
        stole_from, stolen_gifts = gifts_distribution.pop(0)
        gifts_distribution.append((stealer, gifts + stolen_gifts))

        print(len(gifts_distribution))

    return gifts_distribution.pop()[0]


def main():
    print("[Part 1] The winner is %s" % find_white_elephant_winner(CHALLENGE_INPUT))


if __name__ == '__main__':
    main()
