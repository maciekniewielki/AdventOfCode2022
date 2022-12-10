from Common import *


def solve(data):
    regs = {'image': '', 'signal': 0}
    x_val = 1
    cycles = 1
    for line in data:
        if line == 'noop':
            cycles = run_cycle(cycles, x_val, regs)
        else:
            val = int(line.split()[1])
            cycles = run_cycle(cycles, x_val, regs)
            cycles = run_cycle(cycles, x_val, regs)
            x_val += val

    return regs


def run_cycle(cycles, x_val, regs):
    # part 1
    pos = ((cycles - 1) % 40)
    if abs(x_val - pos) <= 1:
        regs['image'] += '#'
    else:
        regs['image'] += '.'
    if cycles % 40 == 0:
        regs['image'] += '\n'

    # part 2
    if cycles in [20, 60, 100, 140, 180, 220]:
        regs['signal'] += cycles * x_val

    return cycles + 1


# IO
a = input_as_lines("input.txt")

# Solving both in one go
regs = solve(a)

# 1st
print(regs['signal'])

# 2nd
print(regs['image'])
