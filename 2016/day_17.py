#!/usr/bin/env python

from hashlib import md5


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
        if 0 <= self.x <= 3 and 0 <= self.y <= 3:
            return True

        return False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

    def distance(self):
        return len(self.visited)

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
    longest_distance = None
    shortest_distance = None
    start = Node(Tile(0, 0), passcode, '')
    nodes = start.adjacents()
    while len(nodes) > 0:
        node = nodes.pop(0)

        if node.position == WIN_POSITION:
            if not shortest_distance:
                shortest_distance = node

            if not longest_distance or len(longest_distance.visited) < len(node.visited):
                longest_distance = node

        else:
            nodes += node.adjacents()

    return shortest_distance.visited, longest_distance.visited


def main():
    shortest, longest = shortest_path('njfxhljp')

    print('[Part 1] %s' % shortest)
    print('[Part 2] %s' % len(longest))


if __name__ == '__main__':
    main()
