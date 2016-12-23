#!/usr/bin/env ruby

require_relative "../day_02"
require "test/unit"

class TestInstructions < Test::Unit::TestCase
	def test_provided
		i = Instructions.new [Digit.load("ULL"), Digit.load("RRDDD"), Digit.load("LURDL"), Digit.load("UUUUD")]

		assert_equal "1985", i.part_1
	end

	def test_provided_b
		i = Instructions.new [Digit.load("ULL"), Digit.load("RRDDD"), Digit.load("LURDL"), Digit.load("UUUUD")]

		assert_equal "5DB3", i.part_2
	end
end
