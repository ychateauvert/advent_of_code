#!/usr/bin/env python

from hashlib import md5
from collections import namedtuple

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Tile(self.x, self.y - 1)

    def down(self):
        return Tile(self.x, self.y + 1)

    def left(self):
        return Tile(self.x - 1, self.y)

    def right(self):
        return Tile(self.x + 1, self.y)

    def is_valid(self):
        if self.x >= 0 and self.x <= 3 and self.y >= 0 and self.y <= 3:
            return True

        return False

    def __repr__(self):
        return "Tile(%s, %s)" % (self.x, self.y)


class Node:
    def __init__(self, position, passcode, visited):
        self.position = position
        self.passcode = passcode
        self.visited = visited

    def full_passcode(self):
        return self.passcode + self.visited

    def go(self, position, name):
        return Node(position, self.passcode, self.visited + name)

    def adjacents(self):
        up, down, left, right = list(map(lambda x: x in 'bcdef', md5(self.full_passcode().encode('utf-8')).hexdigest()[:4]))
        v = []

        if self.position.up().is_valid() and up:
            v.append(self.go(self.position.up(), 'U'))

        if self.position.down().is_valid() and down:
            v.append(self.go(self.position.down(), 'D'))

        if self.position.left().is_valid() and left:
            v.append(self.go(self.position.left(), 'L'))

        if self.position.right().is_valid() and right:
            v.append(self.go(self.position.right(), 'R'))

        return v

    def __repr__(self):
        return "Node: (%s, %s) %s%s" % (self.position.x, self.position.y, self.passcode, self.visited)


WIN_POSITION = Tile(3, 3)


def shortest_path(passcode):
    """ Find shortest path

    >>> shortest_path('ihgpwlah')
    'DDRRRD'

    >>> shortest_path('kglvqrro')
    'DDUDRLRRUDRD'

    >>> shortest_path('ulqzkmiv')
    'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    """
    start = Node(Tile(0, 0), passcode, '')
    nodes = start.adjacents()
    while len(nodes) > 0:
        node = nodes.pop(0)

        if node.position == WIN_POSITION:
            print('')
            print('Found:')
            print(node)
            print(node.visited)

            return node
        else:
            nodes += node.adjacents()


def main():
    room = Room((0,0), 'hijkl')
    adjacents = room.adjacent_rooms()


if __name__ == '__main__':
    main()
