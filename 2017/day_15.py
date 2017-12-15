#!/usr/bin/env python3


def generator_a(seed, part_2=False):
    value = seed
    while True:
        value = (value * 16807) % 2147483647
        if part_2:
            if value % 4 == 0:
                yield value
        else:
            yield value


def generator_b(seed, part_2=False):
    value = seed
    while True:
        value = (value * 48271) % 2147483647
        if part_2:
            if value % 8 == 0:
                yield value
        else:
            yield value


def judge(n, part_2=False):
    matching = 0
    a_creator = generator_a(277, part_2)
    b_creator = generator_b(349, part_2)
    # a_creator = generator_a(65, part_2)
    # b_creator = generator_b(8921, part_2)

    for _ in range(n):
        a = next(a_creator)
        b = next(b_creator)

        # print(a)
        # print(b)

        last_16_a = "{0:b}".format(a).zfill(16)[-16:]
        last_16_b = "{0:b}".format(b).zfill(16)[-16:]
        # print(last_16_a)
        # print(last_16_b)
        if last_16_a == last_16_b:
            matching += 1
        # print('')

    return matching


# print("Part 1: {}".format(judge(40000000)))
print("Part 2: {}".format(judge(5000000, True)))
# print("Part 2: {}".format(judge(5, True)))
