#!/usr/bin/env python3

jumps_offset = [int(x) for x in open("inputs/day_05.txt").read().strip().splitlines()]
# jumps_offset = [0, 3, 0, 1, -3]
last_offset = len(jumps_offset)


def part_a(jumps):
    steps = 0
    index = 0
    while True:
        steps += 1
        next_jump = jumps[index]
        if next_jump + index >= last_offset:
            return steps
        jumps[index] += 1
        index += next_jump


def part_b(jumps):
    steps = 0
    index = 0
    while True:
        steps += 1
        next_jump = jumps[index]
        if next_jump + index >= last_offset:
            return steps
        if next_jump >= 3:
            jumps[index] -= 1
        else:
            jumps[index] += 1
        index += next_jump


print("Part 1: {}".format(part_a(jumps_offset[:])))
print("Part 2: {}".format(part_b(jumps_offset[:])))
