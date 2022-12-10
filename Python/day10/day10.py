from Common import *


def solve(data):
    regs = {'image': '', 'signal': 0}
    xVal = 1
    cycles = 1
    for line in data:
        if line == 'noop':
            cycles = run_cycle(cycles, xVal, regs)
        else:
            val = int(line.split()[1])
            cycles = run_cycle(cycles, xVal, regs)
            cycles = run_cycle(cycles, xVal, regs)
            xVal += val

    return regs


def run_cycle(cycles, xVal, regs):
    # part 1
    pos = ((cycles - 1) % 40)
    if abs(xVal - pos) <= 1:
        regs['image'] += '#'
    else:
        regs['image'] += '.'
    if cycles % 40 == 0:
        regs['image'] += '\n'

    # part 2
    if cycles in [20, 60, 100, 140, 180, 220]:
        regs['signal'] += cycles * xVal

    return cycles + 1


# IO
a = input_as_lines("input.txt")

# Solving both in one go
regs = solve(a)

# 1st
print(regs['signal'])

# 2nd
print(regs['image'])
