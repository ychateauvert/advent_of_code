#!/usr/bin/env ruby

class Word

    def initialize(word)
        @word = word
    end

    def nice?
        vowels = ["a", "e", "i", "o", "u"].inject(0) do |sum, n|
            sum = sum + @word.count(n)
        end

        return false unless vowels >= 3

        return false unless /(.)\1/.match(@word)

        %w{ ab cd pq xy}.each do |dirty|
            if @word.include? dirty
                return false
            end
        end

        true
    end

    def to_s
        @word
    end
end

class NewWord
    def initialize(word)
        @word = word
    end

    def nice?
        return false unless multiple_double

        true
    end

    def multiple_double
        letters = ('a'..'z').map{ |c| c.to_s * 2}
        letters.each do |pair|

        end
        false
    end

    def to_s
        @word
    end
end

contents = File.read("inputs/day_05.txt")

are_nice = 0
are_nice_new = 0 

contents.split("\n").each do |s|
    word = Word.new(s)
    nw = NewWord.new(s)
    if word.nice?
        are_nice = are_nice + 1
    end

    if nw.nice?
        are_nice_new = are_nice_new + 1
        puts nw
    end
end

puts "Nice strings: #{are_nice}"
puts "Nice new strings: #{are_nice_new}"
