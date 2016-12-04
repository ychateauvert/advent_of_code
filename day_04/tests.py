#!/usr/bin/env python3

import unittest

import challenge

def data_provider(fn_data_provider):
    def test_decorator(fn):
        def repl(self, *args):
            for i in fn_data_provider():
                try:
                    fn(self, *i)
                except AssertionError:
                    print("Assert error with data set")
                    raise
        return repl
    return test_decorator


def single_value_provider(data):
    def test_decorator(fn):
        def repl(self, *args):
            for d in data:
                fn(self, d)
        return repl
    return test_decorator


class TestProvidedValues(unittest.TestCase):

    real_rooms = [
            'aaaaa-bbb-z-y-x-123[abxyz]',
            'not-a-real-room-404[oarel]',
            'a-b-c-d-e-f-g-h-987[abcde]'
    ]

    all_rooms = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
        'a-b-c-d-e-f-g-h-987[abcde]'
    ]

    @single_value_provider(real_rooms)
    def test_real_room(self, room):
        self.assertTrue(challenge.is_real(room))

    def test_fake_room(self):
        self.assertFalse(challenge.is_real('totally-real-room-200[decoy]'))

    def test_sector_id_sum(self):
        self.assertEqual(1514, challenge.sum_of_valid_rooms(self.all_rooms))

    def test_decrypt(self):
        self.assertEqual("very encrypted name", challenge.decrypt_room("qzmt-zixmtkozy-ivhz", '343'))

if __name__ == '__main__':
    unittest.main()
