from Common import *


def solve1(cases):
    return sum(one_contains_other(first, second) for first, second in cases)


def one_contains_other(first, second):
    return len(first & second) == min(len(first), len(second))


def solve2(cases):
    return sum(overlap_at_all(first, second) for first, second in cases)


def overlap_at_all(first, second):
    return len(first & second) > 0


def get_numbers_in_section(s):
    bounds = [int(x) for x in s.split('-')]
    return set(range(bounds[0], bounds[1] + 1))


# IO
a = input_as_lines("input.txt")
cases = []
for line in a:
    first, second = line.split(',')
    cases.append([get_numbers_in_section(first),
                 get_numbers_in_section(second)])

# 1st
print(solve1(cases))

# 2nd
print(solve2(cases))
