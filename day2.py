import sys
import re
import functools


class Game:
    def __init__(self, id, handfuls):
        self.id = id
        self.handfuls = handfuls

    pattern = re.compile("^Game (\d+): (.*)$")

    def parse(line):
        match = Game.pattern.match(line)
        game_id = int(match.group(1))
        chunks = match.group(2).split("; ")
        handfuls = []
        for chunk in chunks:
            handful = {}
            components = chunk.split(", ")
            for component in components:
                words = component.split(" ")
                handful[words[1]] = int(words[0])

            handfuls.append(handful)

        return Game(game_id, handfuls)

    def get_minimum_frequencies(self):
        frequencies = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for handful in self.handfuls:
            for colour in handful:
                frequencies[colour] = max(frequencies[colour], handful[colour])

        return frequencies


def is_possible(game: Game, max_frequencies):
    min_frequencies = game.get_minimum_frequencies()
    for colour in max_frequencies:
        if min_frequencies[colour] > max_frequencies[colour]:
            return False

    return True


with open(sys.argv[1]) as f:
    input = [line.strip() for line in f]

games = [Game.parse(line) for line in input]
max_frequencies = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

print("Part 1:", sum(game.id for game in games if is_possible(game, max_frequencies)))
print(
    "Part 2:",
    sum(
        functools.reduce(lambda acc, next: acc * next, frequencies.values())
        for frequencies in [game.get_minimum_frequencies() for game in games]
    ),
)
