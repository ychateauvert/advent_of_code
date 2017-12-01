#!/usr/bin/env python

import asyncio
import subprocess
import os
import sys

from itertools import count

in_values = [x for x in open('inputs/day_25.txt').read().strip().split("\n")]
dir_name = os.getcwd()


class AssemblerProtocol(asyncio.SubprocessProtocol):
    def __init__(self, exit_future):
        self.exit_future = exit_future
        self.output = bytearray()

    def pipe_data_received(self, fd, data):
        self.output.extend(data)

    def process_exited(self):
        self.exit_future.set_result(True)


def is_matching_pattern(a_register_value=0):
    setup_cmd = "cpy %s a" % a_register_value
    input_s = bytes("\n".join([setup_cmd] + in_values).encode('utf-8'))
    with subprocess.Popen(
            [sys.executable, 'day_23.py', '10'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
    ) as process:
        stdout, stderr = process.communicate(input_s)
        v = stdout.decode('ascii').replace("\n", "")
        print(v)
        if v == '0101010101':
            print('Found with %s' % a_register_value)
            return True

    return False


def main():
    for i in count():
        if is_matching_pattern(i):
            print('Pattern %s' % i)
            sys.exit(0)


if __name__ == '__main__':
    main()
