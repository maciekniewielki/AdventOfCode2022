from Common import *

points_for_shape = {"A": 1, "B": 2, "C": 3}


def solve1(rounds):
    return sum(calc_round_one(opponent, mine) for opponent, mine in rounds)


def calc_round_one(opponent, mine):
    to_play = {"X": "A", "Y": "B", "Z": "C"}[mine]
    return calc_win_points(to_play, opponent) + points_for_shape[to_play]


def solve2(rounds):
    return sum(calc_round_two(opponent, strategy) for opponent, strategy in rounds)


def calc_round_two(opponent, strategy):
    to_play = calc_move_for_me(opponent, strategy)
    return calc_win_points(to_play, opponent) + points_for_shape[to_play]


def calc_win_points(me, opponent):
    if (me == "A" and opponent == "B") or (me == "B" and opponent == "C") or (me == "C" and opponent == "A"):
        return 0
    elif me == opponent:
        return 3
    else:
        return 6


def calc_move_for_me(opponent, result):
    if result == "Y":
        # draw
        return opponent
    if result == "Z":
        # win
        if opponent == "A":
            return "B"
        elif opponent == "B":
            return "C"
        else:
            return "A"
    else:
        # lose
        if opponent == "A":
            return "C"
        elif opponent == "B":
            return "A"
        else:
            return "B"


# IO
a = input_as_lines("input.txt")
rounds = [line.split() for line in a]

# 1st
print(solve1(rounds))

# 2nd
print(solve2(rounds))
