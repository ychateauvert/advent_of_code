#!/usr/bin/env python

moves = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def find_intersection(wire_a, wire_b):
    return set(trace_wire(wire_a)).intersection(set(trace_wire(wire_b)))


def calculate_distance(wire_a, wire_b):
    """
    >>> calculate_distance('R8,U5,L5,D3'.split(','), 'U7,R6,D4,L4'.split(','))
    6
    >>> calculate_distance('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','), 'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))
    159
    >>> calculate_distance('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','), 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))
    135
    """
    common = find_intersection(wire_a, wire_b)
    min_distance = min([abs(x) + abs(y) for x, y in common])

    return min_distance


def trace_wire(wire):
    x, y = 0, 0
    locations = []

    for step in wire:
        direction, distance = step[0], int(step[1:])
        delta_x, delta_y = moves[direction]
        for _ in range(distance):
            x += delta_x
            y += delta_y
            locations.append((x, y))

    return locations


def part1():
    wire_a, wire_b = [x.split(',') for x in open('inputs/day_03.txt').read().strip().splitlines()]

    return calculate_distance(wire_a, wire_b)


def part2():
    wire_a, wire_b = [x.split(',') for x in open('inputs/day_03.txt').read().strip().splitlines()]
    wire_a_pos = trace_wire(wire_a)
    wire_b_pos = trace_wire(wire_b)

    common = set(wire_a_pos).intersection(set(wire_b_pos))
    path_to_crossing = []
    for intersection in common:
        wa_len = wire_a_pos.index(intersection) + 1
        wb_len = wire_b_pos.index(intersection) + 1

        path_to_crossing.append(wa_len + wb_len)

    return min(path_to_crossing)


def main():
    # Part 1: 5319
    print(f"Part 1: {part1()}")

    # Part 2: 122514
    print(f"Part 2: {part2()}")


if __name__ == '__main__':
    main()