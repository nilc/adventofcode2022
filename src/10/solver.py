import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import re
from copy import deepcopy

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()
cycle = 0
pos_x = 1
cycle_x = {cycle: pos_x}
addtox = None
for line in lines:
    if addtox is not None:
        pos_x += addtox
        addtox = None
    line = line.strip()
    print(f"{line} status: {cycle} {pos_x}")
    if line == "noop":
        cycle += 1
        cycle_x[cycle] = pos_x
    else:
        addtox = int(line.split(" ")[1])
        for t in range(2):
            cycle += 1
            cycle_x[cycle] = pos_x
sum = 0
print(cycle_x)
for s in [20, 60, 100, 140, 180, 220]:
    s_ = s * cycle_x[s]
    print(f"{s}*{cycle_x[s]}={s_} ")
    sum += s_
print(sum)

for crt_y in range(0, 6):
    line = ""
    for pos_x in range(0, 40):
        crtcycle = crt_y * 40 + pos_x
        pixel_middle = cycle_x[crtcycle+1]
        if pixel_middle + 1 == pos_x or pixel_middle == pos_x or pixel_middle - 1 == pos_x:
            line += "#"
        else:
            line += "."
    print(line)
