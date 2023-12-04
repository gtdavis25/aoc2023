import sys
import re

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f]

pattern = re.compile(r"\d+")
cards = []
for line in input:
    i = 0
    winning_numbers = []
    my_numbers = []
    for match in pattern.finditer(line):
        if i == 0:
            id = int(match.group())
        elif i < 11:
            winning_numbers.append(int(match.group()))
        else:
            my_numbers.append(int(match.group()))

        i += 1

    cards.append((id, winning_numbers, my_numbers))

total = 0
for id, winning_numbers, my_numbers in cards:
    score = 0
    for n in my_numbers:
        if n in winning_numbers:
            score = 1 if score == 0 else score * 2

    total += score

print("Part 1:", total)
quantities = {card[0]: 1 for card in cards}
for id, winning_numbers, my_numbers in cards:
    winning_number_count = 0
    for n in my_numbers:
        if n in winning_numbers:
            winning_number_count += 1

    for i in range(winning_number_count):
        quantities[id + 1 + i] += quantities[id]

print("Part 2:", sum(qty for qty in quantities.values()))
