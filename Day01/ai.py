def sum_of_calibration_values(calibration_document: str) -> int:
    def get_digit(s: str) -> str:
        if s.isdigit():
            return s
        else:
            return str(ord(s) - ord('a') + 1)

    return sum(int(get_digit(line[0]) + get_digit(line[-1])) for line in calibration_document.split())

with open('testfilepart2.txt', 'r') as f:
    calibration_document = f.read()

print(sum_of_calibration_values(calibration_document))