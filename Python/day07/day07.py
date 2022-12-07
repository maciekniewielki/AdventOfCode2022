from Common import *


def solve1(dir_sizes):
    return sum(size for size in dir_sizes if size <= 100000)


def solve2(dir_sizes):
    size_total = max(dir_sizes)
    free_space = 70000000 - size_total
    to_free = 30000000 - free_space
    return find_first_working(sorted(dir_sizes), to_free)


def find_first_working(sizes, to_free):
    for size in sizes:
        if size > to_free:
            return size


def calculate_dir_sizes(data):
    files = find_all_files(data)
    dir_sizes = {}
    for file_path in files:
        cwd = file_path
        while cwd != '/':
            cwd = go_up(cwd)
            if cwd not in dir_sizes:
                dir_sizes[cwd] = 0
            dir_sizes[cwd] += files[file_path]

    return list(dir_sizes.values())


def find_all_files(data):
    files = {}
    cwd = "/"
    for line in data:
        if line.startswith('$'):
            commands = line.split(' ')[1:]
            if commands[0] == 'cd' and commands[1] == '/':
                cwd = '/'
            elif commands[0] == 'cd' and commands[1] == '..':
                cwd = go_up(cwd)
            elif commands[0] == 'cd':
                cwd = go_down(cwd, commands[1])
            elif commands[0] == 'ls':
                continue
        else:
            # in ls
            size, file_name = line.split(' ')
            if size != 'dir':
                full_file_name = go_down(cwd, file_name)
                files[full_file_name] = int(size)
    return files


def go_down(cwd, word):
    if cwd.endswith('/'):
        return cwd + word
    else:
        return cwd + '/' + word


def go_up(cwd):
    up = '/'.join(cwd.split('/')[:-1])
    if not up:
        up = '/'
    return up


# IO
a = input_as_lines("input.txt")


# 1st
dir_sizes = calculate_dir_sizes(a)
print(solve1(dir_sizes))

# 2nd
print(solve2(dir_sizes))
