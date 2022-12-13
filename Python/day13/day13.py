from Common import *
from functools import cmp_to_key


def solve1(data):
    acc = 0
    for i, chunk in enumerate(data):
        index_of_pair = i + 1
        left = eval(chunk[0])
        right = eval(chunk[1])
        if in_order(left, right) == 1:
            acc += index_of_pair
    return acc


def solve2(data):
    div_1 = [[2]]
    div_2 = [[6]]
    vals = [eval(line) for line in data] + [div_1, div_2]
    s = sorted(vals, key=cmp_to_key(in_order), reverse=True)
    index_1, index_2 = s.index(div_1) + 1, s.index(div_2) + 1
    return index_1 * index_2


# -1 not in order, 0 continue, 1 in order
def in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    if isinstance(left, list) and isinstance(right, list):
        if (len(left)) == 0 and len(right) > 0:
            return 1
        if (len(left)) == 0 and len(right) == 0:
            return 0
        for index in range(len(left)):
            if index > len(right) - 1:
                return -1
            comp = in_order(left[index], right[index])
            if comp != 0:
                return comp
            if index == len(left) - 1 and index < len(right) - 1:
                return 1
        return 0
    if isinstance(left, list) and isinstance(right, int):
        return in_order(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return in_order([left], right)


# IO
a = input_as_chunks("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(flatten(a)))
