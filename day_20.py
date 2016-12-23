#!/usr/bin/env python

def main():
    blacklist_intervals = [tuple(map(int, x.split("-"))) for x in open("inputs/day_20.txt").read().strip().split("\n")]

    valid_ips, current_ip, index = 0, 0, 0
    blacklist_intervals.sort()
    while current_ip < 4294967295:
        low, high = blacklist_intervals[index]
        if current_ip >= low:
            if current_ip <= high:
                # If we are within an interval skip to first ip after interval
                current_ip = high + 1
                continue
            index += 1
        else:
            valid_ips += 1
            current_ip += 1


    print("[Part 2] Valid ips %s" % valid_ips)


if __name__ == '__main__':
    main()
