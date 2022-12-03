from Common import *


def solve1(lines):
    return sum(intersect_and_calculate(line[:len(line)//2], line[len(line)//2:]) for line in lines)


def solve2(first, second, third):
    return sum(intersect_and_calculate(*rucksacks) for rucksacks in zip(first, second, third))


def intersect_and_calculate(*rucksacks):
    sets = [set(a) for a in rucksacks]
    return value_of_char(set.intersection(*sets).pop())


def value_of_char(c):
    return (ord(c.lower()) - 96) + c.isupper() * 26


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a[0::3], a[1::3], a[2::3]))
