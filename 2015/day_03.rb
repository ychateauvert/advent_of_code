#!/usr/bin/env ruby

class Santa
    attr_accessor :visited
    attr_reader :name

    def self.start(name, x=0, y=0)
        santa = Santa.new(name)
        santa.visited << Location.new(0, 0)

        santa
    end

    def initialize(name)
        @name = name
        @visited = []
    end

    def current
        @visited[-1]
    end

    def visit(location)
        @visited << location
    end

    def unique_locations
        @visited.uniq { |l| [l.x, l.y] }
    end

    def to_s
        "<Santa #{name}>"
    end
end

class Location
    attr_accessor :x, :y

    def initialize(x, y)
        @x = x
        @y = y
    end

    def eql?(other)
        return @x === other.x && @y === other.y
    end

    def ^
        Location.new(x, y + 1)
    end

    def v
        Location.new(x, y - 1)
    end

    def >
        Location.new(x + 1, y)
    end

    def <
        Location.new(x - 1, y)
    end

    def to_s
        "<Location (#{x}, #{y})>"
    end
end

contents = File.read("inputs/day_03.txt")

santa = Santa.start("santa")
robo_santa = Santa.start("robo")

contents.split("").each_with_index do |chr, index|
    s = case index % 2
        when 0
            santa
        when 1
            robo_santa
        else
            puts "FAIL"
        end
    puts s
    puts chr
    s.visit(s.current.method(chr).call)
end

puts "==============="
puts "Santa"
puts santa.visited
puts "Robo"
puts robo_santa.visited

v = santa.visited.concat(robo_santa.visited)
u = v.uniq { |l| [l.x, l.y] }

puts "Visited: #{v.size}"
puts "Uniques: #{u.size}"
