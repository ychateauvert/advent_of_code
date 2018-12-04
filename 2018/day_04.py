#!/usr/bin/env python

import sys
import re
import datetime
import operator

from collections import defaultdict,Counter

R_DATE = re.compile(r"\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] (.*)")
R_GUARD_ID = re.compile(r"Guard \#(\d+)")


def parse_entry(entry):
    date, hour, minute, description = R_DATE.match(entry).groups()
    return date, int(hour), int(minute), description


def real_shift_date(rotation):
    date, hour, minute, description = rotation

    if hour == 23:
        d = datetime.date(*map(int, date.split('-')))
        d += datetime.timedelta(days=1)

        return d.isoformat()

    return date


def filter_by_day(rotation):
    filtered = defaultdict(list)
    for line in rotation:
        real_date = real_shift_date(line)

        filtered[real_date].append(line)

    return filtered


def find_guard(input_file):
    asleep_minutes_by_guard = defaultdict(list)
    sleeping_minutes = defaultdict(int)
    rotation = [parse_entry(x) for x in open(input_file).read().strip().splitlines()]

    filtered = filter_by_day(rotation)
    for shift_day, shift_actions in filtered.items():
        current_guard_id = False
        sleeping_since = False
        for _, hour, minute, description in shift_actions:
            if description.startswith('Guard'):
                current_guard_id = R_GUARD_ID.match(description).group(1)
                sleeping_since = False
            elif description.startswith('falls asleep'):
                if sleeping_since:
                    print('Debug: double sleeping ?!?!')
                sleeping_since = minute
            elif description.startswith('wakes up'):
                if not sleeping_since and sleeping_since != 0:
                    print('Debug: waking up from not sleeping?!?')
                if not current_guard_id:
                    print('Debug: Shift not started?!?!')
                sleeping_minutes[current_guard_id] += int(minute) - int(sleeping_since)
                asleep_minutes_by_guard[current_guard_id].extend(list(range(int(sleeping_since), int(minute))))
                sleeping_since = False
        if sleeping_since:
            sleeping_minutes[current_guard_id] += 60 - int(sleeping_since)
            asleep_minutes_by_guard[current_guard_id].extend(list(range(int(sleeping_since), 60)))

    best_sleeper = max(sleeping_minutes.items(), key=operator.itemgetter(1))
    c = Counter(asleep_minutes_by_guard[best_sleeper[0]])

    part1 = int(best_sleeper[0]) * c.most_common(1)[0][0]

    part2_counters = { g: Counter(v) for g, v in asleep_minutes_by_guard.items()}
    maxPart2 = False
    for gid, c in part2_counters.items():
        best = c.most_common(1)[0]
        if not maxPart2 or best[1] > maxPart2[1][1]:
            maxPart2 = gid, best

    part2 = int(maxPart2[0]) * maxPart2[1][0]

    return part1, part2


if len(sys.argv) > 1:
    part1, part2 = find_guard(sys.argv[1])
else:
    part1, part2 = find_guard('inputs/day_04.txt')

print('Day 04 part 1: %s' % part1)
print('Day 04 part 2: %s' % part2)
