import sys
from functools import reduce
from math import ceil, floor, log10


def count_winning_ways(time, distance):
    min_hold_time = floor(time / 2)
    if min_hold_time * (time - min_hold_time) <= distance:
        return 0

    lower = 0
    while lower + 1 < min_hold_time:
        mid = floor((lower + min_hold_time) / 2)
        if mid * (time - mid) > distance:
            min_hold_time = mid
        else:
            lower = mid

    return time - 2 * min_hold_time + 1


def concatenate(numbers):
    return reduce(lambda x, y: x * 10 ** ceil(log10(y)) + y, numbers)


with open(sys.argv[1]) as f:
    lines = f.readlines()

times = [int(n) for n in lines[0][len("Time:") :].split()]
distances = [int(n) for n in lines[1][len("Distance:") :].split()]
races = list(zip(times, distances))
winning_way_counts = [count_winning_ways(time, distance) for time, distance in races]
print("Part 1:", reduce(lambda x, y: x * y, winning_way_counts))
print("Part 2:", count_winning_ways(concatenate(times), concatenate(distances)))
