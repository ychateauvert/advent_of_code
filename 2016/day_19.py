#!/usr/bin/env python

from math import floor

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

    return gifts_distribution.pop()[0]


def find_white_elephant_across(participants_count):
    """ Steal across

    >>> find_white_elephant_across(5)
    2
    """
    participants = list(range(1, participants_count+1))
    gifts_distribution = {i: 1 for i in participants}

    while len(participants) > 1:
        stole_from_idx = floor(len(participants)/2)
        # print(participants)
        # print(gifts_distribution)
        stole_from = participants.pop(stole_from_idx)
        stealer = participants.pop(0)

        gifts_distribution[stealer] += gifts_distribution[stole_from]
        gifts_distribution[stole_from] = 0
        participants.append(stealer)
        # print("Stealer: %s, Stolen from %s" % (stealer, stole_from))

    return participants[0]


def main():
    # print("[Part 1] The winner is %s" % find_white_elephant_winner(CHALLENGE_INPUT))
    print("[Part 2] The winner is %s" % find_white_elephant_across(CHALLENGE_INPUT))


if __name__ == '__main__':
    main()
