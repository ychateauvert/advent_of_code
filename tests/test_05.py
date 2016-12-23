#!/usr/bin/env python

import unittest
import day_05

class TestChallenge(unittest.TestCase):

	#def test_provided(self):
		#self.assertEqual('18f47a30', day_05.find_password('abc'))

	def test_part_2(self):
		self.assertEqual('05ace8e3', day_05.find_password('abc', True))

