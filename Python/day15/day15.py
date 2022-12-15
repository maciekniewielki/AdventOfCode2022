from Common import *
import re
import functools


def solve1(data):
    items = set()
    beacons = set()
    sensors = set()
    all_data = parse_data(data)
    y = 2000000
    for line in all_data:
        sensor, beacon, _ = line
        sensors.add(sensor)
        beacons.add(beacon)
        items |= get_taken_points(y, sensor, beacon)
    removed = items - (beacons | sensors)
    return len(removed)


def get_taken_points(y, sensor, beacon):
    taken = set()
    radius = manhattan(sensor, beacon)
    y_diff = abs(sensor[1] - y)
    if y_diff <= radius:
        r = (radius - y_diff)
        for x_coord_offset in range(-r, r + 1):
            taken.add((sensor[0] + x_coord_offset, y))
    if sensor[1] == y:
        taken.add(sensor)
    if beacon[1] == y:
        taken.add(beacon)

    return taken


def solve2(data):
    all_data = parse_data(data)
    for y in range(0, 4000000):
        holes = get_holes_for_y(y, all_data)
        if holes:
            return holes[0] * 4000000 + holes[1]


def parse_data(data):
    all_data = []
    for line in data:
        nums = [int(num) for num in re.findall('[-+]?[0-9]+', line)]
        sensor, beacon = tuple(nums[0:2]), tuple(nums[2:4])
        all_data.append([sensor, beacon, manhattan(sensor, beacon)])
    return all_data


def get_holes_for_y(y, all_data):
    ranges = []
    for l in all_data:
        sensor, _, radius = l
        r = get_taken_range(y, sensor, radius)
        if r:
            ranges.append(r)
    s = sorted(ranges, key=lambda range: range[0])
    try:
        functools.reduce(merge_ranges, s)
        return None
    except Exception as e:
        return (e.args[0], y)


def merge_ranges(r1, r2):
    minimum = min(r1[0], r2[0])
    maximum = max(r1[1], r2[1])
    if r1[1] >= r2[0] - 1:
        return (minimum, maximum)
    # If we are here, there is a gap. We pass gaps x in the exception
    raise Exception(r1[1] + 1)


def get_taken_range(y, sensor, radius):
    y_diff = abs(sensor[1] - y)
    if y_diff <= radius:
        r = (radius - y_diff)
        return (sensor[0] - r, sensor[0] + r)
    return ()


def manhattan(pos1, pos2):
    return sum(abs(x1 - x2) for x1, x2 in zip(pos1, pos2))


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
