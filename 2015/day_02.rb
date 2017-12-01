#!/usr/bin/env ruby

contents = File.read("inputs/day_02.txt")
total_area = 0
total_ribbon = 0

contents.split("\n").each do |values|
    length, width, height = values.split("x").map{|chr| chr.to_i}
    dimensions = [length, width, height].sort

    sides = [length * width, width * height, height * length]
    area = sides.inject(0){ |sum, x| sum + x } * 2 + sides.min
    volume = dimensions.inject(1){|sum, x| sum * x }

    ribbon = (dimensions.take(2).inject(0){|sum, x| sum + x} * 2) + volume

    puts "#{values}: Sides=#{sides}, Volume=#{volume}, Extra=#{sides.min}, Ribbon=#{ribbon}, Area=#{area}"

    total_area = total_area + area
    total_ribbon = total_ribbon + ribbon
end


puts "\nTotal area = #{total_area}"
puts "Total ribbon = #{total_ribbon}"
