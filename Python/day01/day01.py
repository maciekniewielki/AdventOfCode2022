from Common import *

def solve1(data):
    return max(sum(x) for x in data)

def solve2(data):
    return sum(sorted(sum(x) for x in data)[-3:])

# IO
a = input_as_chunked_ints("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
