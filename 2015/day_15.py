#!/usr/bin/env python3

import re


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


def best_recipe(ingredients):
    pass


def main():
    regex = re.compile(r'^(.*): capacity ([-]*\d+), durability ([-]*\d), flavor ([-]*\d), texture ([-]*\d), calories ([-]*\d)')

    test = best_recipe([
        Ingredient('Butterscotch', -1, -2, 6, 3, 8),
        Ingredient('Cinnamon', 2, 3, -2, -1, 3)
    ])

    puzzle = [Ingredient(regex.match(x).groups()) for x in open('inputs/day_15.txt').read().strip().split("\n")]
    print(puzzle)


if __name__ == '__main__':
    main()