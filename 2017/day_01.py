#!/usr/bin/env python3

captcha = list(open('inputs/day_01.txt').read().strip())
halfway_around = int(len(captcha) / 2)

cycling_captcha = captcha * 2

part_1 = 0
part_2 = 0
for i, d in enumerate(captcha):
    if d == cycling_captcha[i+1]:
        part_1 += int(d)

    if d == cycling_captcha[i+halfway_around]:
        part_2 += int(d)

print("Part 1: {}".format(part_1))
print("Part 2: {}".format(part_2))
