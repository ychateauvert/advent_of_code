#!/usr/bin/env python3

from itertools import chain, cycle, accumulate  # last of which is Python 3 only

puzzle_input = 29000000


def factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
            if c * c > n: break
            if n % c: continue
            d, p = (), c
            while not n % c:
                n, p, d = n // c, p * c, d + (p,)
            yield (d)
        if n > 1: yield ((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a * b for a in r for b in e]
    return r


for i in range(1000000000):
    result = sum(factors(i)) * 10

    if result >= puzzle_input:
        print(i)
        exit(0)
