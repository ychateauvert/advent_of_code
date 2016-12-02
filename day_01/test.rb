#!/usr/bin/env ruby

require_relative "main"
require "test/unit"

class TestSeeker < Test::Unit::TestCase
	def test_provided_values
		[
			[%w{ R2 R2 R2 }, 2],
			[%w{ R2 L3 }, 5],
			[%w{ R5 L5 R5 R3 }, 12]
		].each do |d, expected|
			directions = d.map { |i| Direction.new(i) }
			assert_equal expected, Seeker.find_shortest(directions)
		end
	end

	#def test_b
		#directions = %w{ R8 R4 R4 R8 }.map { |i| Direction.new(i) }
		#assert_equal 4, Seeker.closest_visited_twice(directions)
	#end
end
