#!/usr/bin/env python

def main():
    # Stolen from Danksalot2000 on reddit
    result = sum(2 * sum([4,2,0,0][:x]) - 3 for x in range(1,4))
    print("[Part 1] Shortest distance %s" % result)

    result = sum(2 * sum([8,2,0,0][:x]) - 3 for x in range(1,4))
    print("[Part 2] Shortest distance %s" % result)


if __name__ == '__main__':
    main()
