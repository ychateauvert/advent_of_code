#!/usr/bin/env python3

# Demo puzzle
# base_hash_input  = 'flqrgnkx'
# Real puzzle
base_hash_input = 'hwlqcszp'


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


def knot_hash(raw):
    lengths = [ord(x) for x in raw]
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

    return bytes(dense_list).hex()


def hex_to_binary(h):
    return bin(int(h, 16))[2:]


def used_spaces(hash):
    return len(list(filter(lambda x: x == '1', hex_to_binary(hash))))


rows = [used_spaces(knot_hash("{}-{}".format(base_hash_input, i))) for i in range(128)]

print(sum(rows))
