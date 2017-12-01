#!/usr/bin/env python3

import string

PUZZLE_INPUT = 'hxbxwxba'
PUZZLE_INPUT_2 = 'hxbxxyzz'


def increase_password(password):
    """
    >>> increase_password('xx')
    'xy'
    >>> increase_password('xy')
    'xz'
    >>> increase_password('xz')
    'ya'
    >>> increase_password('ya')
    'yb'
    """
    r = list(reversed(password))
    done = False
    next = []
    for c in r:
        if done:
            next.append(c)
        else:
            n = ord(c) + 1
            if n > ord('z'):
                n = ord('a')
            else:
                done = True
            next.append(chr(n))

    return "".join(reversed(next))


def next_password(last_password):
    """
    >>> next_password('abcdefgh')
    'abcdffaa'
    >>> next_password('ghijklmn')
    'ghjaabcc'
    """
    p = last_password
    while True:
        p = increase_password(p)
        if is_valid_password(p):
            return p


def is_valid_password(password):
    """
    >>> is_valid_password('hijklmmn')
    False
    >>> is_valid_password('abbceffg')
    False
    >>> is_valid_password('abbcegjk')
    False
    >>> is_valid_password('abcdffaa')
    True
    >>> is_valid_password('ghjaabcc')
    True
    """
    blacklisted_chars = ['i', 'o', 'l']
    pairs = [x * 2 for x in string.ascii_lowercase]
    letters = list(string.ascii_lowercase)
    increment_pairs = ["".join(x) for x in zip(letters[:], letters[1:], letters[2:])]

    first_rule = any([True for x in increment_pairs if x in password])
    second_rule = not any([True for x in blacklisted_chars if x in password])
    third_rule = sum([True for x in pairs if x in password]) >= 2

    return first_rule and second_rule and third_rule


def main():
    print("Santa's next password: %s", next_password(PUZZLE_INPUT))
    print("Santa's next password: %s", next_password(PUZZLE_INPUT_2))


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
