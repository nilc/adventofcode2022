import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import re
from copy import deepcopy

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

tail_positions = []


def check_is_adjecent(pos1, pos2):
    if pos1 == pos2:
        return True
    elif pos1[0] == pos2[0]:
        return abs(pos1[1] - pos2[1]) == 1
    elif pos1[1] == pos2[1]:
        return abs(pos1[0] - pos2[0]) == 1
    else:
        return abs(pos1[0] - pos2[0]) == 1 and abs(pos1[1] - pos2[1]) == 1


def new_pos(oldpos, dir):
    newpos = deepcopy(oldpos)
    if (dir == "RU"):
        newpos = [oldpos[0] + 1, oldpos[1] + 1]
    elif (dir == "LU"):
        newpos = [oldpos[0] - 1, oldpos[1] + 1]
    elif (dir == "LD"):
        newpos = [oldpos[0] + 1, oldpos[1] - 1]
    elif (dir == "RD"):
        newpos = [oldpos[0] - 1, oldpos[1] - 1]
    elif (dir == "U"):
        newpos[1] = oldpos[1] + 1
    elif (dir == "D"):
        newpos[1] = oldpos[1] - 1
    elif (dir == "R"):
        newpos[0] = oldpos[0] + 1
    elif (dir == "L"):
        newpos[0] = oldpos[0] - 1
    else:
        raise Exception(f"Wrong dir {dir}")
    return newpos


def calculuate_tail(tail, head):
    if check_is_adjecent(head, tail):
        # print(f"{head} and {tail} is already adjacent")
        return tail
    newtailpos = None
    directions_to_test = ["U", "D", "R", "L"]
    if tail[0] != head[0] and tail[1] != head[1]:
        directions_to_test = ["RU", "LU", "LD", "RD"]
    for testdir in directions_to_test:
        if newtailpos is None:
            pos = new_pos(tail, testdir)
            if check_is_adjecent(head, pos):
                # print(f"new dir should be {testdir}")
                newtailpos = pos
        #   else:
        #      print(f"wrong dir {testdir} for {pos} and {head}")
    if (newtailpos == None):
        raise Exception(f"Error could not find way to go for tailpos {tail} head is at {head}")

    print(f"tail went to {newtailpos} head is at {head}")
    return newtailpos


head_positions = []
tailposset = set()


def print_positions():
    search = "\\[(.*), (.*)\\]"
    ys = list(map(lambda t: int(re.search(search, t).group(2)), head_positions))
    xs = list(map(lambda t: int(re.search(search, t).group(1)), head_positions))

    for y in range(max(ys) + 1, min(ys) - 1, -1):
        line = ""
        for x in range(min(xs), max(xs) + 1):
            pos = f"{[x, y]}"
            if pos in head_positions and pos in tailposset:
                line = line + ("B")
            elif pos in head_positions:
                line = line + ("H")
            elif pos in tailposset:
                line = line + ("#")
            else:
                line = line + (".")
        print(line)


headpos = [0, 0]

ropetail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for line in lines:
    command = re.search(r"(.) (\d+)", line)
    dir = command.group(1)
    steps = int(command.group(2))

    for i in range(steps):
        head_positions.append(f"{headpos}")
        headpos = new_pos(headpos, dir)
        print(f"{headpos} {line}")

        infront = deepcopy(headpos)
        for tailindex in range(0, len(ropetail)):
            atailpos = ropetail[tailindex]
            print(f"index {tailindex} has pos {atailpos}")
            tail = calculuate_tail(tail=atailpos, head=infront)
            ropetail[tailindex] = tail
            infront = deepcopy(tail)
        tailposset.add(f"{ropetail[8]}")
#print_positions()
print(len(set(head_positions)))
print(len(tailposset))
