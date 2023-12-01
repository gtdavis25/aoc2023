import sys
import re

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f]

digits = [[int(c) for c in line if "0" <= c and c <= "9"] for line in input]
calibration_values = [10 * d[0] + d[len(d) - 1] for d in digits]
print("Part 1:", sum(calibration_values))
words = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digits(line: str):
    digits = []
    for i in range(len(line)):
        for word in words:
            if line[i:].startswith(word):
                digits.append(words[word])
                break

    return digits


digits = [get_digits(line) for line in input]
calibration_values = [10 * d[0] + d[len(d) - 1] for d in digits]
print("Part 2:", sum(calibration_values))
