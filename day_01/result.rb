#!/usr/bin/env ruby

require_relative "main.rb"

directions = File.read("input.txt").split(", ").map { |i| Direction.new(i) } 
a = Seeker.find_shortest directions
puts "Shortest (A): #{a}"

b = Seeker.closest_visited_twice directions
puts "Shortest (B): #{b}"
