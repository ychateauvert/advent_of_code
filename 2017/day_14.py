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
    return '{:0128b}'.format(int(h, 16))


def used_spaces(row):
    return len(list(filter(lambda x: x == '1', hex_to_binary(row))))


def number_of_regions(grid):
    coordinates = []
    for y, row in enumerate(grid):
        for x, value in enumerate(hex_to_binary(row)):
            if value == '1':
                coordinates.append((x, y))

    regions = find_regions(coordinates)

    return len(regions)


def neighbor(coordinate):
    x, y = coordinate

    coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x, y) for x, y in coords if 0 <= x < 128 and 0 <= y < 128]


def find_siblings(coordinates, block):
    seen = set()
    to_checks = list()
    to_checks.append(block)
    while len(to_checks) > 0:
        checked = to_checks.pop()
        for n in neighbor(checked):
            if n in coordinates and n not in seen:
                to_checks.append(n)

        seen.add(checked)

    return seen


def find_regions(coordinates):
    regions = []
    coordinates = coordinates[:]
    while len(coordinates) > 0:
        coord = coordinates.pop()
        region = find_siblings(coordinates, coord)
        regions.append(region)
        for c in region:
            if c in coordinates:
                coordinates.remove(c)
    return regions


rows = [knot_hash("{}-{}".format(base_hash_input, i)) for i in range(128)]

print("Part 1: {}".format(sum([used_spaces(i) for i in rows])))
print("Part 2: {}".format(number_of_regions(rows)))
