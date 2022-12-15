import dataclasses
import json
import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from collections.abc import Sequence
from copy import deepcopy

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

rockpaths = {}


@dataclasses.dataclass
class pos():
    x: int
    y: int


def to_pos(vertex):
    vertex = vertex.split(",")
    return pos(x=int(vertex[0]), y=int(vertex[1]))


def addrock(x, y):
    if (y not in rockpaths):
        rockpaths[y] = {}
    rockpaths[y][x] = '#'


for line in lines:
    vertexs = line.split("->")
    for i in range(len(vertexs) - 1):
        start = to_pos(vertexs[i])
        end = to_pos(vertexs[i + 1])
        for xs in range(min([start.x, end.x]), max([start.x, end.x]) + 1):
            addrock(xs, start.y)
        for ys in range(min([start.y, end.y]), max([start.y, end.y]) + 1):
            addrock(start.x, ys)

        print(rockpaths)


def flatten(l):
    return [item for sublist in l for item in sublist]


def print_state():
    global y, line, x
    allx = flatten(map(lambda ys: rockpaths[ys].keys(), rockpaths.keys()))
    maxx = max(allx)
    minx = min(allx)
    for y in range(0, max(rockpaths.keys()) + 1):
        line = ""
        for x in range(minx, maxx + 1):
            if anything_on_pos(x, y):
                line += rockpaths[y][x]
            else:
                line += " "
        print(line)


def anything_on_pos(x, y, floor=None):
    if (y == floor):
        return True

    return y in rockpaths and x in rockpaths[y]


print_state()


def poursand(x, y):
    if y > max(rockpaths.keys()):
        return False
    if not anything_on_pos(x, y + 1):
        return poursand(x, y + 1)
    elif not anything_on_pos(x - 1, y + 1):
        return poursand(x - 1, y + 1)
    elif not anything_on_pos(x + 1, y + 1):
        return poursand(x + 1, y + 1)
    else:
        if y not in rockpaths:
            rockpaths[y] = {}
        rockpaths[y][x] = 'o'
        return True


def poursand_withfloor(x, y, floor):
    if y > floor:
        return pos(x,y)
    if not anything_on_pos(x, y + 1, floor):
        return poursand_withfloor(x, y + 1,floor)
    elif not anything_on_pos(x - 1, y + 1, floor):
        return poursand_withfloor(x - 1, y + 1, floor)
    elif not anything_on_pos(x + 1, y + 1, floor):
        return poursand_withfloor(x + 1, y + 1, floor)
    else:
        if y not in rockpaths:
            rockpaths[y] = {}
        rockpaths[y][x] = 'o'
        return pos(x,y)


def solve_part1():
    part1_solution = 0
    for i in range(9999):
        should_continue = poursand(500, 0)
        if not should_continue:
            part1_solution=i
            print_state()
            print(i)
            break



#solve_part1()
floor = max(rockpaths.keys()) + 2
for i in range(9999999):
    endpos = poursand_withfloor(500, 0, floor)
    if endpos.x==500 and endpos.y==0:
        print_state()
        print(i+1)
        break


