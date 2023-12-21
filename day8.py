import sys
from functools import reduce


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


nodes = {}
with open(sys.argv[1]) as f:
    lines = f.readlines()
    instructions = lines[0].strip()
    for line in lines[2:]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]


def get_step_count(start_point, suffix):
    position = start_point
    step_count = 0
    while not position.endswith(suffix):
        direction = instructions[step_count % len(instructions)]
        step_count += 1
        position = nodes[position][0 if direction == "L" else 1]

    return step_count


print("Part 1:", get_step_count("AAA", "ZZZ"))
cycle_lengths = [get_step_count(start, "Z") for start in nodes if start.endswith("A")]
print("Part 2", reduce(lcm, cycle_lengths))
