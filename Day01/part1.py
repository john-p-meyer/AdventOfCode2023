def create_2_digit_number(num: str) -> int:
    """
    Given a string `num`, returns a 2 digit number based off the the first numerical digit and the last numerical digit.
    If the line only has 1 digit, use it twice.
    """
    first_digit = None
    last_digit = None
    for char in num:
        if char.isdigit():
            if first_digit is None:
                first_digit = int(char)
            last_digit = int(char)
    if first_digit is None:
        first_digit = last_digit
    return int(str(first_digit) + str(last_digit))

def sum_of_2_digit_numbers(file_path: str) -> int:
    """
    Given a file path `file_path`, returns the sum of 2 digit numbers created from each line in the file.
    """
    total = 0
    with open(file_path, 'r') as f:
        for line in f:
            total += create_2_digit_number(line.strip())
    return total

# Example usage
# file_path = 'testfile.txt'
file_path = 'puzzle.txt'
total = sum_of_2_digit_numbers(file_path)
print(f'Total: {total}')
