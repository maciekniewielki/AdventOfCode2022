from Common import *
import networkx as nx


def solve1(data):
    g = get_graph(data)
    starting_point = find_letter(data, 'S').pop()
    ending_point = find_letter(data, 'E').pop()
    return nx.dijkstra_path_length(g, starting_point, ending_point, weight='distance')


def solve2(data):
    g = get_graph(data)
    starting_points = find_letter(data, 'a')
    ending_point = find_letter(data, 'E').pop()
    return min(nx.dijkstra_path_length(g, start, ending_point, weight='distance') for start in starting_points)


def get_graph(data):
    vertices = set()
    g = nx.DiGraph()
    for curr_x, l in enumerate(data):
        for curr_y, _ in enumerate(l):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if valid_index(curr_x+dx, curr_y+dy, data) and abs(dx) != abs(dy) and (curr_x, curr_y, curr_x+dx, curr_y+dy) not in vertices:
                        vertices.add((curr_x, curr_y, curr_x+dx, curr_y+dy))
                        g.add_edge((curr_x, curr_y), (curr_x+dx, curr_y+dy),
                                   distance=get_dist(data[curr_x][curr_y], data[curr_x+dx][curr_y+dy]))
    return g


def valid_index(i, j, array):
    return 0 <= i < len(array) and 0 <= j < len(array[i])


def get_dist(a, b):
    a, b = convert_to_elevation(a), convert_to_elevation(b)
    if ord(b) - ord(a) <= 1:
        return 1
    else:
        return 9999999


def convert_to_elevation(a):
    if a == 'S':
        return 'a'
    if a == 'E':
        return 'z'
    return a


def find_letter(data, letter):
    points = set()
    for curr_x, l in enumerate(data):
        for curr_y, _ in enumerate(l):
            if data[curr_x][curr_y] == letter:
                points.add((curr_x, curr_y))
    return points


# IO
a = input_as_lines("input.txt")


# 1st
print(solve1(a))

# 2nd
print(solve2(a))
