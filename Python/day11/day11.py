from Common import *
import re


def solve(data, length, worry_limit_override):
    monkeys = get_monkeys(data)
    for _ in range(length):
        for i in range(len(monkeys)):
            complete_turn(monkeys, i, worry_limit_override)
    s = sorted(monkeys, key=lambda m: m['n_inspects'])
    return s[-1]['n_inspects'] * s[-2]['n_inspects']


def complete_turn(monkeys, i, worry_limit_override):
    combined_modulo = 1
    for m in monkeys:
        combined_modulo *= m['div_test']
    m = monkeys[i]
    for item in list(m['items']):
        old = item
        new = eval(m['operation'])
        if not worry_limit_override:
            new = new // 3
        if new % m['div_test'] == 0:
            target_items = monkeys[m['if_true_throw_to']]['items']
        else:
            target_items = monkeys[m['if_false_throw_to']]['items']

        if worry_limit_override:
            new = new % combined_modulo
        target_items.append(new)
        m['items'].remove(item)
        m['n_inspects'] += 1


def get_monkeys(chunks):
    return [get_monkey(c) for c in chunks]


def get_monkey(chunk):
    starting_items = list(map(int, re.findall('[0-9]+', chunk[1])))
    operation = re.findall('= (.*)$', chunk[2])[0]
    div_test = int(re.findall('[0-9]+', chunk[3])[0])
    if_true_throw_to = int(re.findall('[0-9]+', chunk[4])[0])
    if_false_throw_to = int(re.findall('[0-9]+', chunk[5])[0])
    return {
        'items': starting_items,
        'operation': operation,
        'div_test': div_test,
        'if_true_throw_to': if_true_throw_to,
        'if_false_throw_to': if_false_throw_to,
        'n_inspects': 0
    }


# IO
a = input_as_chunks("input.txt")


# 1st
print(solve(a, 20, False))

# 2nd
print(solve(a, 10000, True))
