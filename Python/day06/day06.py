from Common import *


def solve(data, size):
    for i in range(size, len(data)):
        if len(set(data[i-size: i])) == size:
            return i


# IO
a = input_as_string("input.txt")


# 1st
print(solve(a, 4))

# 2nd
print(solve(a, 14))
