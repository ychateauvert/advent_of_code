#!/usr/bin/env python3

import itertools


def main():
    in_values = [x.split(",") for x in open("inputs/day_9_processed.py").read().strip().split("\n")]
    weighted_edges = [(x[0], x[1], float(x[2])) for x in in_values]
    path = {}
    locations = []

    for orig, dest, distance in weighted_edges:
        path[orig + dest] = distance
        path[dest + orig] = distance

        locations.append(orig)
        locations.append(dest)

    locations = set(locations)

    # Shortest
    shortest_route = 999999999
    longest_route = 0
    for route in itertools.permutations(locations):
        route_length = sum(map(lambda x: path[x[0] + x[1]], zip(route[:-1], route[1:])))

        if route_length < shortest_route:
            shortest_route = route_length

        if route_length > longest_route:
            longest_route = route_length

    print("Shortest route %s", shortest_route)
    print("Longest route %s", longest_route)


if __name__ == '__main__':
    main()
