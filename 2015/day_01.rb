#!/usr/bin/env ruby

floor = 0

contents = File.read("inputs/day_01.txt")

contents.split("").each_with_index do |c, index|
    if c == "("
        floor = floor + 1
    else
        floor = floor - 1
    end
    if floor == -1
        puts index
    end
end

puts floor
