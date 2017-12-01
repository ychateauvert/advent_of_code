#!/usr/bin/env python3

GRID_LENGTH = 100

PART_2 = True

demo_puzzle = [
    ".#.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####..",
]

coordinates = [(x, y) for y in range(GRID_LENGTH) for x in range(GRID_LENGTH)]
neighboors_relative = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def how_many_neighboor_on(p, coordinate):
    neighbors = [(coordinate[0]+x, coordinate[1]+y) for x, y in neighboors_relative]
    return sum([p[n] for n in neighbors if n in p])


def toggle_puzzle(p):
    new_p = dict()
    for coord, value in p.items():
        new_val = False

        how_many = how_many_neighboor_on(p, coord)

        if value:
            if how_many == 2 or how_many == 3:
                new_val = True
        else:
            if how_many == 3:
                new_val = True

        if PART_2:
            if coord in [(0,0), (0, 99), (99, 0), (99, 99)]:
                new_val = True
            # if coord in [(0,0), (0, 5), (5, 0), (5, 5)]:
            #     new_val = True


        new_p[coord] = new_val

    return new_p


def get_status_coordinates(p, coord):
    return p[coord[1]][coord[0]] == '#'


def set_status_coordinate(p, coord, status):
    val = '.'
    if status:
        val = '#'
    row = list(p[coord[1]])
    row[coord[0]] = val
    p[coord[1]] = "".join(row)


def puzzle_to_dict(p):
    new_p = dict()
    for y, row in enumerate(p):
        for x, column in enumerate(row):
           new_p[(x, y)]  = column == '#'

    return new_p


def dict_to_puzzle(d):
    p = []
    for y in range(GRID_LENGTH):
        column = []
        # column = [d[(x, y)] for x in range(GRID_LENGTH)]
        for x in range(GRID_LENGTH):
            value = '.'
            if d[(x, y)]:
                value = '#'
            column.append(value)
        p.append("".join(column))

    return p


def print_puzzle(d):
    p = dict_to_puzzle(d)
    for row in p:
        print(row)


# puzzle = puzzle_to_dict(demo_puzzle)
puzzle = puzzle_to_dict([x for x in open('inputs/day_18.txt').read().strip().split("\n")])
print('Initial')

puzzle[(0, 0)] = True
puzzle[(0, 99)] = True
puzzle[(99, 0)] = True
puzzle[(99, 99)] = True

print_puzzle(puzzle)
for i in range(1, 101):
    puzzle = toggle_puzzle(puzzle)
    print("Step {}:".format(i))
    print_puzzle(puzzle)
    print("Lights on: {}".format(sum(puzzle.values())))

