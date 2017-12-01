#!/usr/bin/env ruby

require "digest/md5"

secret_key = "iwrupvqb"
digit = 0

while true do
    v = secret_key + digit.to_s
    md5 = Digest::MD5.hexdigest(v)
    #puts "Key #{v}, md5: #{md5}"

    if md5[0..5] === "000000"
        puts digit
        exit
    end

    digit = digit + 1
end
