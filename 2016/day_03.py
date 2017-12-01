#!/usr/bin/env python

from pprint import pprint
import numpy as np

def valid_triangle(sides):
    if len(sides) < 3:
        return False

    a, b, c = sorted(sides)

    return a < b + c and b < a + c and c < a + b

def part_1():
    in_value = [list(map(int, t.split())) for t in open("inputs/day_03.txt").read().split("\n")]
    valid_triangles = list(filter(valid_triangle, in_value))
    print (len(valid_triangles))

def is_valid(sides):
    if len(sides) < 3:
        return False

    a, b, c = sorted(sides)

    return a < b + c and b < a + c and c < a + b

def part_2():
    in_values = np.array(list(filter(lambda x: len(x) == 3, [list(map(int, t.split())) for t in open("input.txt").read().split("\n")])))

    valid_triangles = 0

    for column in in_values.T:
        valid_triangles = valid_triangles + sum([is_valid(t) for t in np.split(column, len(column) / 3)])

    print(valid_triangles)
