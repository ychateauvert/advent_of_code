#!/usr/bin/env python3

import sys
import math
import itertools

BIG_NUM = int(math.sqrt(289326))

data_location = 289326

bottom_right = 537
side = 539

def squares():
    for i in itertools.count(1, 2):
        yield i * i


layer = 0
for i in squares():
    print("{}: {}".format(layer, i))
    layer += 1
    if i >= data_location:
        sys.exit()

# Rest done on paper and with the help of lookup table:
# https://oeis.org/A141481/b141481.txt
