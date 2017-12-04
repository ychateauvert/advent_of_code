#!/usr/bin/enb python3

import collections


def is_valid_part_b(passphrase):
    by_length = collections.defaultdict(list)
    for i in passphrase:
        by_length[len(word)].append(collections.Counter(i))

    for l, words in by_length.items():
        while len(words) > 0:
            last = words.pop()
            if last in words:
                return False

    return True


passphrases = [x.split() for x in open("inputs/day_04.txt").read().strip().splitlines()]

valid = 0

for word in [collections.Counter(x) for x in passphrases]:
    most = word.most_common(1)
    w, c = most[0]
    if c <= 1:
        valid += 1

print("Part 1: {}".format(valid))
print("Part 2: {}".format(sum([is_valid_part_b(x) for x in passphrases])))

