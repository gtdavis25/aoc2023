import sys


def get_next_value(sequence):
    if all(n == 0 for n in sequence):
        return 0

    differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    return sequence[len(sequence) - 1] + get_next_value(differences)


def get_previous_value(sequence):
    if all(n == 0 for n in sequence):
        return 0

    differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    return sequence[0] - get_previous_value(differences)


with open(sys.argv[1]) as f:
    sequences = [[int(word) for word in line.split()] for line in f]

print("Part 1:", sum(get_next_value(sequence) for sequence in sequences))
print("Part 2:", sum(get_previous_value(sequence) for sequence in sequences))
