#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+?\d+|\w+)/).join + "," + ARGV[0].scan(/to:(\+?\d+|\w+)/).join + "," + ARGV[0].scan(/flags:([0-9 -:]+)/).join
