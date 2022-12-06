import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import re

import string

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()


listofset = []
sum = 0

dict = {}



def pretty_print_dict(a_dict: dict):
    l = list(a_dict.keys())
    l.sort()
    for x in l:
        if len(a_dict[x]) > 0:
            print(a_dict[x][0])


def move_crates(to_move, from_stack, to_stack, dict):
    print(dict)
    f_stack = dict[from_stack]
    moved_crates = []
    for i in range(0, to_move):
        moved_crates.append(f_stack.pop(0))
    dict[to_stack]=moved_crates + dict[to_stack]
    print(dict)


for line in lines:
    if "[" in line:
        for x in range(0, len(line), 4):
            print(x)
            if line[x] == "[":
                stack_no = int(x / 4) + 1
                if stack_no not in dict:
                    dict[stack_no] = []
                arrayen = dict[stack_no]
                arrayen.append(line[x + 1])
    if "move" in line:
        # move 1 from 2 to 1
        result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        to_move = int(result.group(1))
        from_stack = int(result.group(2))
        to_stack = int(result.group(3))
        move_crates(to_move, from_stack, to_stack, dict)
pretty_print_dict(dict)
