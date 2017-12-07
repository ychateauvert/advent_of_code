#!/usr/bin/env python3

import sys

memory_banks = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
# memory_banks = [0, 2, 7, 0]


def find_first_highest_memory_index(banks):
    return banks.index(max(banks))


def next_index(banks, i):
    n = i + 1
    if n >= len(banks):
        n = 0

    return n


def redistribute(banks):
    banks = banks[:]
    highest_index = find_first_highest_memory_index(banks)
    remaining_value_to_redistribute = banks[highest_index]
    banks[highest_index] = 0

    i = next_index(banks, highest_index)
    while remaining_value_to_redistribute > 0:
        banks[i] += 1

        i = next_index(banks, i)
        remaining_value_to_redistribute -= 1

    return banks


def hash_banks(banks):
    return "".join([str(x) for x in banks])


def solutions(memory):
    memory = memory[:]
    founds = list()
    founds.append("".join(hash_banks(memory)))
    cycles = 0
    while True:
        memory = redistribute(memory)
        cycles += 1
        h = hash_banks(memory)
        if h in founds:
            return (cycles, len(founds) - founds.index(h))
        founds.append(h)


p_1, p_2 = solutions(memory_banks)

print("Part 1: {}".format(p_1))
print("Part 1: {}".format(p_2))

