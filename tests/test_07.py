#!/usr/bin/env python

import unittest
from day_07 import IpAddress

def data_provider(data_provider):
    def decorator(fn):
        def repl(self, *args):
            for i in data_provider:
                fn(self, *i)
        return repl
    return decorator

class TestChallege(unittest.TestCase):

    provided_part_1 = [
        (IpAddress('abba[mnop]qrst'), True),
        (IpAddress('abcd[bddb]xyyx'), False),
        (IpAddress('aaaa[qwer]tyui'), False),
        (IpAddress('ioxxoj[asdfgh]zxcvbn'), True)
    ]

    provided_part_2 = [
        (IpAddress('aba[bab]xyz'), True),
        (IpAddress('xyx[xyx]xyx'), False),
        (IpAddress('aaa[kek]eke'), True),
        (IpAddress('zazbz[bzb]cdb'), True)
    ]


    # @data_provider(provided_part_1)
    # def test_provided_part_1(self, ip_address, supportTls):
        # self.assertEqual(supportTls, ip_address.is_supporting_tls())

    @data_provider(provided_part_2)
    def test_provided_part_2(self, ip_address, supportSsl):
        self.assertEqual(supportSsl, ip_address.is_supporting_ssl())

