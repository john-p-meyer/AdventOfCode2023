def replace_strings_with_numbers(line):
    replacements = {
        "oneight": 18,
        "threeight": 38,
        "fiveight": 58,
        "nineight": 98,
        "sevenine": 79,
        "eightwo": 82,
        "eighthree": 83,
        "twone": 21,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for string, number in replacements.items():
        line = line.replace(string, str(number))
    return line

def create_two_digit_number(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) == 1:
        digits.append(digits[0])
    print(int(digits[0] + digits[-1]))
    return int(digits[0] + digits[-1])

def process_file(file_path):
    total = 0
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            print(line)
            line = replace_strings_with_numbers(line)
            total += create_two_digit_number(line)
    return total

total = process_file("puzzle.txt")
print(total)
