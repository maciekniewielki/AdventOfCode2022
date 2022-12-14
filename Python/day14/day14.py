from Common import *


def solve1(data):
    blocked_lines = get_blocked_lines(data)
    blocked_points = get_blocked_points(blocked_lines)
    acc = 0
    sand_pos = (500, 0)
    while True:
        next_pos = get_next_sand_pos(sand_pos, blocked_points, None)
        if next_pos:
            sand_pos = next_pos
        else:
            blocked_points.add(sand_pos)
            acc += 1
            sand_pos = (500, 0)
        if sand_pos[1] > 1000:
            break
    return acc


def solve2(data):
    blocked_lines = get_blocked_lines(data)
    blocked_points = get_blocked_points(blocked_lines)
    ground_pos = max(blocked_points, key=lambda point: point[1])[1] + 2
    acc = 0
    sand_pos = (500, 0)
    while True:
        next_pos = get_next_sand_pos(sand_pos, blocked_points, ground_pos)
        if next_pos:
            sand_pos = next_pos
        else:
            blocked_points.add(sand_pos)
            acc += 1
            if sand_pos == (500, 0):
                break
            sand_pos = (500, 0)
    return acc


def get_next_sand_pos(curr_sand_pos, blocked, ground_pos):
    if ground_pos and curr_sand_pos[1] + 1 == ground_pos:
        return None

    down = (curr_sand_pos[0], curr_sand_pos[1] + 1)
    down_left = (curr_sand_pos[0] - 1, curr_sand_pos[1] + 1)
    down_right = (curr_sand_pos[0] + 1, curr_sand_pos[1] + 1)

    if down not in blocked:
        return down
    elif down_left not in blocked:
        return down_left
    elif down_right not in blocked:
        return down_right
    else:
        return None


def get_blocked_lines(data):
    all_lines = set()
    for line in data:
        points = line.split(' -> ')
        for pair_from, pair_to in zip(points[:-1], points[1:]):
            all_lines.add((to_coord(pair_from), to_coord(pair_to)))
    return all_lines


def to_coord(pair):
    x, y = pair.split(',')
    return int(x), int(y)


def get_blocked_points(blocked_lines):
    blocked = set()
    for l in blocked_lines:
        start, end = l
        blocked |= get_points_in_line(start, end)
    return blocked


def get_points_in_line(start, end):
    if start[0] == end[0]:
        begin, end = min(start[1], end[1]), max(start[1], end[1])
        return set((start[0], x) for x in range(begin, end+1))
    if start[1] == end[1]:
        begin, end = min(start[0], end[0]), max(start[0], end[0])
        return set((x, start[1]) for x in range(begin, end+1))


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
