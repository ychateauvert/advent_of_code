#!/usr/bin/env python3

puzzle = open('inputs/day_10.txt').read().strip().split(',')
reverse_instructions = [int(x) for x in puzzle]


def reverse_sub(lst, start, end):
    sublist = []
    for i in range(start, end + 1):
        sublist.append(lst[i % len(lst)])
    reverse = list(reversed(sublist))
    j = 0
    for i in range(start, end + 1):
        lst[i % len(lst)] = reverse[j]
        j += 1

    return lst

lengths = list(map(int, reverse_instructions))
numbers = [x for x in range(0, 256)]
index = 0
skip = 0

for l in lengths:
    numbers = reverse_sub(numbers, index, index + l - 1)
    index += (l + skip)
    skip += 1

print("Part 1: {}".format(numbers[0] * numbers[1]))


# Part 2
lengths = [ord(x) for x in open('inputs/day_10.txt').read().strip()]
lengths.extend([17, 31, 73, 47, 23])
numbers = list(range(0, 256))
index = 0
skip = 0

for _ in range(64):
    for l in lengths:
        numbers = reverse_sub(numbers, index, index + l - 1)
        index += (l + skip)
        skip += 1

dense_list = []
for i in range(16):
    for j in range(16):
        if j == 0:
            acc = numbers[(i*16) + j]
        else:
            acc = acc ^  numbers[(i*16) + j]
    dense_list.append(acc)

print("Part 2: {}".format(bytes(dense_list).hex()))

