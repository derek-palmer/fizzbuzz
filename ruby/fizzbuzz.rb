# Write a program that prints the numbers from 1 to  100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz.”

require 'colorize'

1.upto(100) do |i|
  if i % 3 == 0 and i % 5 == 0
    puts 'FizzBuzz'.blue
  elsif i % 3 == 0
    puts 'Fizz'.red
  elsif i % 5 == 0
    puts 'Buzz'.yellow
  else
    puts i
  end
end
