#!/usr/bin/env ruby

require_relative "bathroom"

instructions = Instructions.load_from_file "input.txt"

puts "A: #{instructions.part_1}"
puts "B: #{instructions.part_2}"
