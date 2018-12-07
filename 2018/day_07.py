#!/usr/bin/env python

import collections
import itertools
import re
import string

R_STEPS = re.compile(r"Step (\w+) must be finished before step (\w)+ can begin.")


def is_valid(value, graph):
    """

    :param value:
    :param graph:
    :return:
    >>> is_valid('CABDFE', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    True
    >>> is_valid('ABCDEF', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    False
    >>> is_valid('', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    True
    """
    previous = []
    for char in value:
        if not all(x in previous for x in graph[char]) and len(graph[char]) != 0:
            return False

        previous.append(char)

    return True


def resolve(graph):
    step_names = graph.keys()
    remaining = collections.deque([('', step_names)])

    while len(remaining) > 0:
        current, missing_steps = remaining.pop()
        if len(missing_steps) == 0:
            return current

        valids = []
        for missing_step in missing_steps:
            checked, missing_after_pop = next_step = (current + missing_step, [x for x in missing_steps if x != missing_step])
            if is_valid(checked, graph):
                valids.append(next_step)

        if len(valids) > 1:
            remaining.append(sorted(valids)[0])
        else:
            remaining.append(valids[0])


def part_1(filename):
    """

    :param filename:
    :return:
    >>> part_1('tests/day_07.txt')
    'CABDFE'
    """
    assembly_dependencies = [R_STEPS.match(x).groups() for x in open(filename).read().strip().splitlines()]
    step_names = {x for x in itertools.chain.from_iterable(assembly_dependencies)}
    dependency_graph = {x: set() for x in step_names}

    for dependency, step in assembly_dependencies:
        dependency_graph[step].add(dependency)

    return resolve(dependency_graph)


def available_steps(current, graph):
    """

    :param current:
    :param graph:
    :return:
    >>> available_steps('CABDFE', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    []
    >>> available_steps('', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    ['C']
    >>> available_steps('CA', {'D': {'A'}, 'E': {'F', 'D', 'B'}, 'F': {'C'}, 'A': {'C'}, 'C': set(), 'B': {'A'}})
    ['B', 'D', 'F']
    """
    remaining = [x for x in graph.keys() if x not in current]

    if len(remaining) == 0:
        return []

    a = sorted([x for x in remaining if all(y in current for y in graph[x])])
    return a


def part_2(filename, no_of_workers, delay=60):
    """

    >>> part_2('tests/day_07.txt', 2, 0)
    15
    """
    assembly_dependencies = [R_STEPS.match(x).groups() for x in open(filename).read().strip().splitlines()]
    step_names = {x for x in itertools.chain.from_iterable(assembly_dependencies)}
    dependency_graph = {x: set() for x in step_names}

    for dependency, step in assembly_dependencies:
        dependency_graph[step].add(dependency)

    numeric_letter_value = dict(zip(string.ascii_uppercase, range(1, 27)))

    current = ''
    second = 0
    workers = []
    while True:
        new_workers = []
        for letter, wait_until in workers:
            if wait_until == second:
                current += letter
            else:
                new_workers.append((letter, wait_until))
        workers = new_workers

        steps = available_steps(current, dependency_graph)
        if len(steps) == 0:
            return second
        elif len(steps) == 0 and len(current) != len(dependency_graph.keys()):
            return 'broken'

        steps_being_processed = [x[0] for x in workers]
        steps_to_be_assigned = sorted([x for x in steps if x not in steps_being_processed], reverse=True)
        while len(workers) < no_of_workers and len(steps_to_be_assigned) > 0:
            next_step = steps_to_be_assigned.pop()
            workers.append((next_step, second + delay + numeric_letter_value[next_step]))

        second += 1


if __name__ == '__main__':
    print('Day 07 part 1: %s' % part_1('inputs/day_07.txt'))

    print('Day 07 part 2: %s' % part_2('inputs/day_07.txt', 5))
