#!/usr/bin/env ruby

$keypad = {
	:U => [nil, nil, nil, 1, 2, 3, 4, 5, 6],
	:D => [4, 5, 6, 7, 8, 9, nil, nil, nil],
	:R => [2, 3, nil, 5, 6, nil, 8, 9, nil],
	:L => [nil, 1, 2, nil, 4, 5, nil, 7, 8]
}

$keypad2 = {
	:U => [nil, nil, 1, nil, nil, 2, 3, 4, nil, 6, 7, 8, 11],
	:D => [3, 6, 7, 8, nil, 10, 11, 12, nil, nil, 13, nil, nil],
	:R => [nil, 3, 4, nil, 6, 7, 8, 9, nil, 11, 12, nil, nil],
	:L => [nil, nil, 2, 3, nil, 5, 6, 7, 8, nil, 10, 11, nil]
}

$pad = $keypad

class Direction
	def initialize(value)
		@value = value
	end

	def to_s
		case @value
		when "U"
			return "Up"
		when "D"
			return "Down"
		when "L"
			return "Left"
		when "R"
			return "Right"
		end
	end

	def to_s
		@value
	end

	def to_sym
		@value.to_sym
	end
end

class Digit
	def initialize(directions)
		@directions = directions
	end

	def self.load(directions) 
		Digit.new directions.split("").map { |i| Direction.new i }
	end

	def resolve(starting_key)
		current = starting_key
		@directions.each do |direction|
			#puts "Direction #{direction}"
			#puts "From: #{current}"
			#puts "To go #{direction.to_sym}"
			#puts $pad[direction.to_sym].size
			#puts "Debug: #{$pad[direction.to_sym][current - 1]}"
			new_pos = $pad[direction.to_sym][current - 1]
			current = new_pos unless new_pos.nil?
			#puts "To: #{current}"
			#puts
		end
		#puts "Found Digit: #{current}"
		current
	end

	def to_s
		"Digit directions: #{@directions.join(" ")}"
	end
end

class Instructions
	attr_reader :digits

	def initialize(digits)
		@digits = digits
	end

	def translate(digit)
		return digit.to_s unless digit > 9
		case digit
		when 10
			return "A"
		when 11
			return "B"
		when 12
			return "C"
		when 13
			return "D"
		end
	end

	def resolve_pin(pad, starting_key = 5)
		current_key = starting_key
		$pad = pad
		v = @digits.map { |d| current_key = d.resolve(current_key) }
		v.map { |i| translate i }.join("")
	end

	def self.load_from_file(filename)
		Instructions.new File.read(filename).split("\n").map { |i| Digit.load i }
	end

	def part_1
		resolve_pin $keypad
	end

	def part_2
		resolve_pin $keypad2
	end
end

instructions = Instructions.load_from_file "inputs/day_02.txt"

puts "A: #{instructions.part_1}"
puts "B: #{instructions.part_2}"
