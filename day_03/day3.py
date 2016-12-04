#!/usr/bin/env python

from pprint import pprint

def valid_triangle(sides):
    if len(sides) < 3:
        return False

    a, b, c = sorted(sides)

    return a < b + c and b < a + c and c < a + b

in_value = [list(map(int, t.split())) for t in open("input.txt").read().split("\n")]
valid_triangles = list(filter(valid_triangle, in_value))
print (len(valid_triangles))
