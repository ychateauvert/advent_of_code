#!/usr/bin/env python



def score(stream):
    """
    :param stream:
    :return:

    >>> score('{}')
    (1, 1)
    >>> score('{{{}}}')
    (6, 3)
    >>> score('{{},{}}')
    (5, 3)
    >>> score('{{{},{},{{}}}}')
    (16, 6)
    >>> score('{<{},{},{{}}>}')
    (1, 1)
    >>> score('{<a>,<a>,<a>,<a>}')
    (1, 1)
    >>> score('{{<a>},{<a>},{<a>},{<a>}}')
    (9, 5)
    >>> score('{{<!>},{<!>},{<!>},{<a>}}')
    (3, 2)
    """
    # Totals
    score = 0
    groups = 0
    # Track current depth
    current_group = 0
    # Is the next value ignored?
    next_is_ignored = False
    # Are we in garbage data?
    in_garbage = False
    for char in stream:
        if in_garbage:
            if next_is_ignored:
                next_is_ignored = False
                continue
            if char == '!':
                next_is_ignored = True
            elif char == '>':
                in_garbage = False
        else:
            if char == '{':
                current_group += 1
            elif char == '}':
                score += current_group
                current_group -= 1
                groups +=1
            elif char == '<':
                in_garbage = True

    return score, groups


def removed_garbage(stream):
    """
    :param stream:
    :return:

    >>> removed_garbage('<>')
    0
    >>> removed_garbage('<random characters>')
    17
    >>> removed_garbage('<<<<>')
    3
    >>> removed_garbage('<{!>}>')
    2
    >>> removed_garbage('<!!>')
    0
    >>> removed_garbage('<!!!>>')
    0
    >>> removed_garbage('<{o"i!a,<{i<a>')
    10
    """
    removed_chars = 0
    # Is the next value ignored?
    next_is_ignored = False
    # Are we in garbage data?
    in_garbage = False
    for char in stream:
        if in_garbage:
            if next_is_ignored:
                next_is_ignored = False
                continue
            if char == '!':
                next_is_ignored = True
            elif char == '>':
                in_garbage = False
            else:
                removed_chars += 1
        else:
            if char == '{':
                pass
            elif char == '}':
                pass
            elif char == '<':
                in_garbage = True

    return removed_chars


# import doctest
# doctest.testmod()

char_stream = open('inputs/day_09.txt').read().strip()
print("Part 1: {}".format(score(char_stream)))

print("Part 2: {}".format(removed_garbage(char_stream)))
