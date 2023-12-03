import sys
import re

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f]

number_pattern = re.compile(r"\d+")
symbol_pattern = re.compile(r"[^\d\.]")
numbers = []
symbols = []
for y in range(len(input)):
    line = input[y]
    for match in number_pattern.finditer(line):
        numbers.append(
            {
                "value": int(match.group()),
                "row": y,
                "offset": match.start(),
                "length": match.end() - match.start(),
            }
        )

    for match in symbol_pattern.finditer(line):
        symbols.append(
            {
                "value": match.group(),
                "row": y,
                "offset": match.start(),
                "part_numbers": [],
            }
        )

for symbol in symbols:
    for number in numbers:
        if (
            abs(number["row"] - symbol["row"]) < 2
            and symbol["offset"] <= number["offset"] + number["length"]
            and number["offset"] <= symbol["offset"] + 1
        ):
            symbol["part_numbers"].append(number["value"])

print("Part 1:", sum(sum(symbol["part_numbers"]) for symbol in symbols))
print(
    "Part 2:",
    sum(
        gear["part_numbers"][0] * gear["part_numbers"][1]
        for gear in symbols
        if gear["value"] == "*" and len(gear["part_numbers"]) == 2
    ),
)
