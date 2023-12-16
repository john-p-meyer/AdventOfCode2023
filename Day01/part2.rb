def replace_strings_with_numbers(line)
    replacements = {
        "oneight" => "18",
        "threeight" => "38",
        "fiveight" => "58",
        "nineight" => "98",
        "sevenine" => "79",
        "eightwo" => "82",
        "eighthree" => "83",
        "twone" => "21",
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9"
    }

    replacements.each do |word, number|
        line = line.gsub(word, number)
    end

    return line
end

def create_2_digit_number(num)
    first_digit = nil
    last_digit = nil

    num.each_char do |char|
      if char.to_i != 0 || char == "0"
        if first_digit == nil
            first_digit = char
        end
        last_digit = char
      end
    end

    return (first_digit + last_digit).to_i
end

def sum_of_2_digit_numbers(file_path)
    total = 0

    lines = File.read(file_path).split("\n")

    lines.each do |line|
        total += create_2_digit_number(replace_strings_with_numbers(line))      
    end

    return total
end

file_path = "puzzle.txt"
total = sum_of_2_digit_numbers(file_path)
puts "Total: #{total}"