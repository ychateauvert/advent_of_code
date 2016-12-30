#!/usr/bin/env python

import networkx as nx
from itertools import permutations

POS_RANGE = [-1, 1]


class HVAC:
    def __init__(self, values):
        self.raw = values

    def visit_all_fewest(self):
        # Manual parsing of graph in favor of networkx
        graph_height, graph_width = len(self.raw), len(self.raw[0])
        G = nx.generators.classic.grid_2d_graph(graph_width, graph_height)

        distances = dict()
        locations = dict()

        for y in range(graph_height):
            for x in range(graph_width):
                char = self.raw[y][x]
                if char == '#':
                    G.remove_node((x, y))
                elif char is not '.':
                    locations[int(char)] = (x, y)

        locations_cnt = len(locations)
        for i in range(locations_cnt):
            for j in range(locations_cnt):
                distances[i, j] = distances[j, i] = nx.shortest_path_length(G, locations[i], locations[j])

        best = 1000000000
        best_part_2 = 1000000000
        for p in permutations(range(1, locations_cnt)):
            path = [0] + list(p)
            totals = sum(distances[path[i+1], path[i]] for i in range(locations_cnt-1))
            best = min(totals, best)
            best_part_2 = min(best_part_2, totals + distances[path[locations_cnt-1], 0])

        return best, best_part_2

    @staticmethod
    def from_file(filename):
        return HVAC(
            open(filename).read().strip().split("\n")
        )

if __name__ == '__main__':
    hvac = HVAC.from_file('inputs/day_24.txt')

    part_1, part_2 = hvac.visit_all_fewest()
    print('[Part 1] %s' % part_1)
    print('[Part 2] %s' % part_2)
