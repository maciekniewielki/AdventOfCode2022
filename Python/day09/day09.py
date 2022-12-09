from Common import *


def solve(data, length):
    knots = [(0, 0) for _ in range(length)]
    visited = set()
    for line in data:
        direction, amount = line.split()
        amount = int(amount)
        knots, tail_positions = move(direction, amount, knots)
        visited = visited | tail_positions
    return len(visited)


def move(direction, amount, knots):
    tail_positions = set([knots[-1]])
    knots = knots[:]
    for _ in range(amount):
        head = knots[0]
        if direction == "R":
            head = (head[0] + 1, head[1])
        elif direction == "L":
            head = (head[0] - 1, head[1])
        elif direction == "U":
            head = (head[0], head[1] + 1)
        elif direction == "D":
            head = (head[0], head[1] - 1)
        knots[0] = head

        for head_i in range(len(knots) - 1):
            tail_i = head_i + 1
            curr_head = knots[head_i]
            curr_tail = knots[tail_i]
            knots[tail_i] = update_tail(curr_head, curr_tail)
        tail_positions.add(knots[-1])
    return knots, tail_positions


def update_tail(head, tail):
    if head[0] == tail[0] or head[1] == tail[1]:
        # right
        if (head[0] - tail[0] > 1):
            return (head[0] - 1, tail[1])

        # left
        if (tail[0] - head[0] > 1):
            return (head[0] + 1, tail[1])

        # up
        if (head[1] - tail[1] > 1):
            return (tail[0], head[1] - 1)

        # down
        if (tail[1] - head[1] > 1):
            return (tail[0], head[1] + 1)
    elif abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        # equal diagonal
        return ((head[0] + tail[0])//2, (head[1] + tail[1])//2)
    else:
        # weird diagonals
        if (head[0] - tail[0] > 1):
            return (tail[0] + 1, head[1])

        if (tail[0] - head[0] > 1):
            return (tail[0] - 1, head[1])

        if (head[1] - tail[1] > 1):
            return (head[0], tail[1] + 1)

        if (tail[1] - head[1] > 1):
            return (head[0], tail[1] - 1)
    return tail


# IO
a = input_as_lines("input.txt")


# 1st
print(solve(a, 2))

# 2nd
print(solve(a, 10))
