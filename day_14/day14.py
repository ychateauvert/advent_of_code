#!/usr/bin/env python

import sys
import pdb
import re
from hashlib import md5

SALT = "ngcjuoqr"
# SALT = "abc"

R_TRIPLE = re.compile(r"([a-zA-Z0-9]{1})\1\1")

hashes_queue = []

def stretched(fn):
    def wrapper(value):
        h = fn(value)
        for _ in range(2016):
            h = md5(h.encode('utf-8')).hexdigest()

        return h
    return wrapper


@stretched
def hash_value(raw):
    return md5(raw.encode('utf-8')).hexdigest()


def hash_generator():
    global hashes_queue

    # We want at least one item in the list for the while loop
    if len(hashes_queue) == 0:
        raw = SALT + "0"
        hashes_queue += [(hash_value(raw), 0)]

    while True:
        while len(hashes_queue) != 1001:
            _, last_index = hashes_queue[-1]
            index = last_index + 1
            raw = SALT + str(index)
            hashes_queue += [(hash_value(raw), index)]

        yield hashes_queue.pop(0) # Pop the first element, still have 1000 hashes in queue


def key_generator():
    for h, index in hash_generator():
        triple = R_TRIPLE.search(h)
        if triple:
            for checked, i in hashes_queue:
                if str(triple.group(1)) * 5 in checked:
                    yield (h, index)
                    break


def main():
    keys = [x for x in zip(range(64), key_generator())]
    for i in keys:
        print(i)


if __name__ == '__main__':
    main()
