#!/usr/bin/env python

from collections import Counter

def decrypt(repetitions):
    frequencies = dict()
    for word in repetitions:
        for i, letter in enumerate(word):
            if i not in frequencies:
                frequencies[i] = []
            frequencies[i].append(letter)

    return [Counter(frequencies[x]) for x in frequencies]

def part_1(repetitions):
    return "".join([x.most_common(1)[0][0] for x in decrypt(repetitions)])

def part_2(repetitions):
    return "".join([x.most_common()[-1][0] for x in decrypt(repetitions)])


def main():
    repetitions = open("input.txt").read().split("\n")

    print("[Part 1] The word is %s" % part_1(repetitions))
    print("[Part 2] The word is %s" % part_2(repetitions))


if __name__ == '__main__':
    main()
