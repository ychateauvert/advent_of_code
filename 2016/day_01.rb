#!/usr/bin/env ruby

require "test/unit"

class Orientation
	def self.left_of(face)
		case face
		when :north
			return :west
		when :east
			return :north
		when :south
			return :east
		when :west
			return :south
		end
	end

	def self.right_of(face)
		case face
		when :north
			return :east
		when :east
			return :south
		when :south
			return :west
		when :west
			return :north
		end
	end
end

class Direction
	attr_reader :raw, :orientation, :distance

	def initialize(raw)
		@raw = raw
		@orientation = raw[0]
		@distance = raw[1..raw.size].to_i
	end

	def to_s
		"Direction: #{orientation} -> #{distance}"
	end
end

class Position
	attr_reader :x, :y

	def initialize(x, y)
		@x = x.to_i
		@y = y.to_i
	end

	def shortest_distance
		@x.abs + @y.abs
	end

	def to_s
		"<Position (#{x},#{y})>"
	end
end

class Seeker
	attr_reader :visited

	def initialize
		@current = Position.new(0, 0)
		@facing = :north
		@visited = [@current]
	end

	def follow(directions)
		directions.each do |direction|
			if direction.orientation == "L"
				o = Orientation.left_of(@facing)
			else
				o = Orientation.right_of(@facing)
			end

			old_pos = @current
			old_face = @facing


			turn o
			advance direction.distance

			puts "#{direction}: Pos=#{old_pos}, #{old_face} -> #{o}, #{@current}"
		end

		@current
	end

	def turn(face)
		@facing = face
	end

	def advance(distance)
		x = @current.x
		y = @current.y

		(1..distance).each do |i|

			case @facing
			when :north
				@current = Position.new(x, y + i)
			when :south
				@current = Position.new(x, y - i)
			when :east
				@current = Position.new(x + i, y)
			when :west
				@current = Position.new(x - i, y)
			end

			@visited.push @current
		end
	end

	def self.find_shortest(directions)
		s = Seeker.new
		final = s.follow directions
		final.shortest_distance
	end


	def self.closest_visited_twice(directions)
		s = Seeker.new
		s.follow directions

		h = Hash.new(0)
		s.visited.each do |pos|
			h[pos.to_s] += 1
			if h[pos.to_s] > 1
				return pos.shortest_distance
			end
		end
	end

	def to_s
		"Seeker: Current=#{@current}, Visited=#{@visited.size}"
	end
end

directions = File.read("inputs/day_01.txt").split(", ").map { |i| Direction.new(i) } 
a = Seeker.find_shortest directions
puts "Shortest (A): #{a}"

b = Seeker.closest_visited_twice directions
puts "Shortest (B): #{b}"
