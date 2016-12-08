#!/usr/bin/env python

from itertools import repeat
import re

class Panel:

    def __init__(self, width, height):
        self.grid = [["."] * width for row in range(height)]

    def display(self):
        return ["".join(row) for row in self.grid]

    def rect(self, width, height):
        for row_id in range(height):
            for column_id in range(width):
                self.lit(column_id, row_id)


    def rotate_column(self, column, quantity):
        column = int(column)
        quantity = int(quantity)
        for _ in repeat(None, quantity):
            new_grid = [list(x) for x in self.grid]
            for i, row in enumerate(self.grid):
                next_row_id = i + 1
                if next_row_id > len(self.grid) - 1:
                    next_row_id = 0

                new_grid[next_row_id][column] = row[column]
            self.grid = new_grid

    def rotate_row(self, row, quantity):
        row = int(row)
        self.grid[row] = self.grid[row][-quantity:] + self.grid[row][:-quantity]


    def swipe(self, instructions, animate=False):
        if animate:
            self.print()
        for i in instructions:
            print()
            print(i)

            if re.match('rect', i):
                width, height = re.search(r"rect (\d+)x(\d+)", i).group(1, 2)
                self.rect(int(width), int(height))
            elif re.match('rotate column', i):
                column, distance = re.search(r"rotate column x=(\d+) by (\d+)", i).group(1, 2)
                if animate:
                    print("Column[%s] -> %s" % (column, distance))
                self.rotate_column(column, distance)
            elif re.match('rotate row', i):
                row, distance = re.search(r"rotate row y=(\d+) by (\d+)", i).group(1, 2)
                if animate:
                    print("Row[%s] -> %s" % (row, distance))
                self.rotate_row(int(row), int(distance))



            self.print()
        pass

    def lit_pixels(self):
        return sum([i.count("#") for i in self.display()])

    def lit(self, x, y):
        self.grid[y][x] = '#'

    def unlit(self, x, y):
        self.grid[y][x] = '.'

    def print(self):
        for row in self.grid:
            print("".join(row))
        print('-' * len(self.grid[0]))


def main():
    instructions = open("input.txt").read().split("\n")
    panel = Panel(50, 6)
    panel.swipe(instructions, animate=True)

    print("[Part 1] Number of lit pixels: %s" % panel.lit_pixels())


if __name__ == '__main__':
    main();
