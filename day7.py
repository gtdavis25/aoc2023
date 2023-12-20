import sys
from functools import cmp_to_key

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1


def compare_hands(first, second, include_jokers=False):
    if include_jokers:
        first_type = get_hand_type(replace_jokers(first))
        second_type = get_hand_type(replace_jokers(second))
    else:
        first_type = get_hand_type(first)
        second_type = get_hand_type(second)

    if first_type != second_type:
        return first_type - second_type

    first_values = get_card_values(first)
    second_values = get_card_values(second)
    for i in range(len(first_values)):
        if first_values[i] != second_values[i]:
            return first_values[i] - second_values[i]

    return 0


def get_hand_type(hand):
    card_frequencies = get_card_frequencies(hand)
    if 5 in card_frequencies:
        return FIVE_OF_A_KIND

    if 4 in card_frequencies:
        return FOUR_OF_A_KIND

    if 3 in card_frequencies:
        return FULL_HOUSE if 2 in card_frequencies else THREE_OF_A_KIND

    if 2 in card_frequencies:
        return TWO_PAIR if len(card_frequencies) < 4 else ONE_PAIR

    return HIGH_CARD


def get_card_frequencies(hand):
    card_frequencies = {}
    for card in hand:
        if card not in card_frequencies:
            card_frequencies[card] = 0

        card_frequencies[card] += 1

    return card_frequencies.values()


CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def get_card_values(hand):
    return [CARD_VALUES[hand[i]] for i in range(len(hand))]


def get_total_winnings(hands):
    hands = [(hand, bid, rank) for rank, (hand, bid) in enumerate(hands, start=1)]
    return sum(bid * rank for _, bid, rank in hands)


def replace_jokers(hand):
    freqs = {}
    for card in hand:
        if card != "J":
            if card not in freqs:
                freqs[card] = 0

            freqs[card] += 1

    most_frequent = "A"
    for card in freqs:
        if most_frequent not in freqs or freqs[card] > freqs[most_frequent]:
            most_frequent = card

    return hand.replace("J", most_frequent)


with open(sys.argv[1]) as f:
    hands = [(words[0], int(words[1])) for words in [line.split() for line in f]]


hands.sort(key=cmp_to_key(lambda first, second: compare_hands(first[0], second[0])))
print("Part 1:", get_total_winnings(hands))
CARD_VALUES["J"] = 1
hands.sort(
    key=cmp_to_key(
        lambda first, second: compare_hands(first[0], second[0], include_jokers=True)
    )
)

print("Part 2:", get_total_winnings(hands))
