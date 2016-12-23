#!/usr/bin/env python

import re
from collections import defaultdict

provided_part_1 = [
    "value 5 goes to bot 2",
    "bot 2 gives low to bot 1 and high to bot 0",
    "value 3 goes to bot 1",
    "bot 1 gives low to output 1 and high to bot 0",
    "bot 0 gives low to output 2 and high to output 0",
    "value 2 goes to bot 2"
]


def parse_line(line):
    splitted = line.strip().split(" ")
    if splitted[0] == 'bot':
        return ('give', int(splitted[1]), (splitted[5], int(splitted[6])), (splitted[10], int(splitted[11])))
    elif splitted[0] == 'value':
        return ('value', int(splitted[5]), int(splitted[1]))
    print(line)


def part_1(instructions):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    actions = {}

    for i in instructions:
        if i[0] == 'value':
            _, bot_id, chip = i
            bots[bot_id].append(chip)
        if i[0] == 'give':
            _, who, low, high = i
            actions[who] = (low, high)

    while bots:
        for k, bot in dict(bots).items():
            if len(bot) == 2:
                low_val, high_val = sorted(bots.pop(k))
                if low_val == 17 and high_val == 61:
                    print('Found it: %s %s' % (k, bot))
                low, high = actions[k]
                if (low[0] == 'bot'):
                    bots[low[1]].append(low_val)
                else:
                    outputs[low[1]].append(low_val)

                if (high[0] == 'bot'):
                    bots[high[1]].append(high_val)
                else:
                    outputs[high[1]].append(high_val)
    print("Outputs 0,1,2: %s" % (outputs[0][0] * outputs[1][0] * outputs[2][0]))
    print(outputs)

def main():
    in_values = map(parse_line, open('inputs/day_10.txt').read().split('\n'))
    r = part_1([x for x in in_values if x])
    print(r)

if __name__ == '__main__':
    main()
