from Common import *


def solve1(data):
    return sum(1 if visible(data, i, j) else 0 for i, j in iter(data))


def iter(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            yield i, j


def visible(data, i, j):
    if is_edge(data, i, j):
        return True

    val = data[i][j]
    for c in get_chunks(data, i, j):
        if val > max(c):
            return True

    return False


def vert_slice(data, i_from, i_to, j):
    return [line[j] for i, line in enumerate(data) if i_from <= i < i_to]


def get_chunks(data, i, j):
    return [
        vert_slice(data, 0, i, j)[::-1],
        vert_slice(data, i+1, len(data), j),
        (data[i][:j])[::-1],
        data[i][j+1:]
    ]


def is_edge(data, i, j):
    return i == len(data) - 1 or j == len(data[0]) - 1 or i * j == 0


def solve2(data):
    return max(calc_score(data, i, j) for i, j in iter(data))


def calc_score(data, i, j):
    if is_edge(data, i, j):
        return 0

    val = data[i][j]
    mult = 1
    for c in get_chunks(data, i, j):
        acc = 0
        for tmp in c:
            acc += 1
            if tmp >= val:
                break
        mult *= acc

    return mult


# IO
a = [[int(c) for c in line] for line in input_as_lines("input.txt")]


# 1st
print(solve1(a))

# 2nd
print(solve2(a))
