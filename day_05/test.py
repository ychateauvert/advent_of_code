#!/usr/bin/env python

import unittest
import challenge

class TestChallenge(unittest.TestCase):

	#def test_provided(self):
		#self.assertEqual('18f47a30', challenge.find_password('abc'))

	def test_part_2(self):
		self.assertEqual('05ace8e3', challenge.find_password('abc', True))

if __name__ == '__main__':
		unittest.main()
