#!/usr/bin/env python

import re
import string

from collections import Counter

ROOM_R = re.compile("(.+)-([0-9]+)\[(.+)\]")

def split_components(room):
    return ROOM_R.match(room).groups()

def is_real(room):
    try:
        name, sector, checksum = split_components(room)
        counter = dict(Counter(name.replace('-', '')))
        frequencies = {}
        for char, value in counter.items():
            if value in frequencies.keys():
                frequencies[value].append(char)
            else:
                frequencies[value] = [char]

        # print("[%s]NAME=%s,SID=%s,CHECKSUM=%s  %s" % (room, name, sector, checksum, counter))

        order = []
        for freq in sorted(frequencies, reverse=True):
            order = order + sorted(frequencies[freq])

        return not any([char not in order[:5] for char in checksum])
    except:
        return False

def translate(letter, sid):
    large_dict = string.ascii_lowercase * 100

    if letter not in string.ascii_lowercase:
        return " "

    index = string.ascii_lowercase.find(letter)
    return large_dict[index + int(sid)]

def valid_rooms(rooms):
    return [room for room in rooms if is_real(room)]

def decrypt_room(name, sid):
    return "".join([translate(x, sid) for x in name])

def sum_of_valid_rooms(rooms):
    return sum(map(lambda x: int(split_components(x)[1]), valid_rooms(rooms)))

def storage_location(in_values):
    decrypted = [(decrypt_room(room, split_components(room)[1]), room) for room in valid_rooms(in_values)]
    for d, room in decrypted:
        if "north" in d:
            return (room, d)
def main():
    in_values = open("inputs/day_04.txt").read().split("\n")
    print("Part 1: Sum of valid rooms SID: %s" % sum_of_valid_rooms(in_values))
    print("Part 2: Decrypted rooms name: %s %s" % storage_location(in_values))


if __name__ == '__main__':
    main()
