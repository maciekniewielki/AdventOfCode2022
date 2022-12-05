from Common import *
import re


def solve(stack_lines, moves, move):
    stacks = get_starting_stacks(stack_lines)
    for c in moves:
        nums = [int(x) for x in re.findall('[0-9]+', c)]
        move(stacks, *nums)
    return ''.join([s[-1] for s in stacks])


def move1(stacks, how_much, from_place, to_place):
    for _ in range(how_much):
        stacks[to_place-1].append(stacks[from_place-1].pop())


def move2(stacks, how_much, from_place, to_place):
    stacks[to_place-1].extend(stacks[from_place-1][-how_much:])
    del stacks[from_place-1][-how_much:]


def get_starting_stacks(lines):
    stacks = [[] for _ in range(n_stacks)]
    for line in lines[:max_stack_height]:
        for offset in range(n_stacks):
            letter = line[4*offset+1]
            if letter != ' ':
                stacks[offset].insert(0, letter)
    return stacks


# IO
a = input_as_lines("input.txt")
empty_line_index = a.index('')
max_stack_height = empty_line_index - 1
n_stacks = int(re.findall('[0-9]+', a[empty_line_index-1])[-1])
stack_lines = a[:empty_line_index-1]
moves = a[empty_line_index+1:]


# 1st
print(solve(stack_lines, moves, move1))

# 2nd
print(solve(stack_lines, moves, move2))
