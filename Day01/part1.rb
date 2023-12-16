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
        total += create_2_digit_number(line)      
    end

    return total
end

file_path = "puzzle.txt"
total = sum_of_2_digit_numbers(file_path)
puts "Total: #{total}"