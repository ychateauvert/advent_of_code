#!/usr/bin/env python3

PUZZLE_INPUT = 1113222113


def look_and_say(puzzle):
    """
    >>> look_and_say(1)
    '11'
    >>> look_and_say(11)
    '21'
    >>> look_and_say(21)
    '1211'
    >>> look_and_say(1211)
    '111221'
    >>> look_and_say(111221)
    '312211'
    """
    puzzle = str(puzzle)
    occ = []
    repeating = 0
    last_char = None
    for c in puzzle:
        if c != last_char and last_char != None:
            occ.append((str(last_char), str(repeating)))
            repeating = 0

        last_char = c
        repeating = repeating + 1

    occ.append((str(c), str(repeating)))

    return "".join([x[1] + x[0] for x in occ])



def main():
    p = PUZZLE_INPUT
    for _ in range(40):
        p = look_and_say(p)

    print("Part 1: %s", len(p))

    p = PUZZLE_INPUT
    for _ in range(50):
        p = look_and_say(p)

    print("Part 2: %s", len(p))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
