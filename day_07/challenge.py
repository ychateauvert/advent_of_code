#!/usr/bin/env python

import re
import pdb

R_SSL = re.compile(r"(.)([^\1])\1(\w*\W\w*\W)*\w*\W\w*\2\1\2")

class IpAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def hypernet_sequences(self):
        return re.findall(r"\[([A-Za-z0-9_]+)\]", self.ip_address)

    def abba_sequences(self):
        return [x.group(0) for x in re.finditer(r"(.)((?!\1).)\2\1", self.ip_address)]

    def is_supporting_tls(self):
        abbas = self.abba_sequences()

        if (len(abbas) < 1):
            return False

        for abba in abbas:
            for hypernet in self.hypernet_sequences():
                if abba in hypernet:
                    return False

        return True

    def is_supporting_ssl(self):
        return len(list(R_SSL.finditer(self.ip_address))) > 0


def main():
    in_values = [IpAddress(x) for x in open("input.txt").read().split("\n")]

    print("[Part 1] IPs supporting TLS: %s" % len([x for x in in_values if x.is_supporting_tls()]))
    print("[Part 2] IPs supporting SSL: %s" % len([x for x in in_values if x.is_supporting_ssl()]))


if __name__ == '__main__':
    main()
