import json
import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from collections.abc import Sequence

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

pairs = []
pair = []
for line in lines:
    line = line.strip()
    if len(line) > 0:
        array = json.loads(line)
        pair.append(array)
    else:
        pairs.append({"left": pair[0], "right": pair[1]})
        pair = []
pairs.append({"left": pair[0], "right": pair[1]})


def isint(list):
    type = int
    return all_is_correct_type(list, type)


def islist(list):
    type = Sequence
    return all_is_correct_type(list, type)


def all_is_correct_type(list, type):
    for l in list:
        if not isinstance(l, type):
            return False
    return True


def compare_pair_arr(leftarr, rightarr):
    print(f"Compare {leftarr} vs {rightarr}")
    for index in range(max(len(rightarr),len(leftarr))):
        if index >= len(rightarr):
            return False
        if index < len(leftarr):
            left = leftarr[index]
            right = rightarr[index]
            print(f"Compare {left} vs {right}")
            if (isint([left, right])):
                if left < right:
                    return True
                if left > right:
                    return False
            else:
                if isinstance(left, Sequence) and not isinstance(right, Sequence):
                    right=[right]
                elif not isinstance(left, Sequence) and isinstance(right, Sequence):
                    left=[left]
                result = compare_pair_arr(left, right)
                if result is not None:
                    return result
        else:
            return True  # left list is empty

inorder = 0
i = 0
for pair in pairs:
    isinrightorder = compare_pair_arr(pair["left"], pair["right"])
    i += 1
    if (isinrightorder):
        inorder += i
    print(f"{i}:{pair} is in order:{isinrightorder}")
print(inorder)
