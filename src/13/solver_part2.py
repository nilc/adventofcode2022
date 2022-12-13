import json
import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from collections.abc import Sequence
from copy import deepcopy

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()
divider_packets=[[[2]], [[6]]]
pairs = deepcopy(divider_packets)
for line in lines:
    line = line.strip()
    if len(line) > 0:
        array = json.loads(line)
        pairs.append(array)


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
    # print(f"Compare {leftarr} vs {rightarr}")
    for index in range(max(len(rightarr), len(leftarr))):
        if index >= len(rightarr):
            return False
        if index < len(leftarr):
            left = leftarr[index]
            right = rightarr[index]
            # print(f"Compare {left} vs {right}")
            if (isint([left, right])):
                if left < right:
                    return True
                if left > right:
                    return False
            else:
                if isinstance(left, Sequence) and not isinstance(right, Sequence):
                    right = [right]
                elif not isinstance(left, Sequence) and isinstance(right, Sequence):
                    left = [left]
                result = compare_pair_arr(left, right)
                if result is not None:
                    return result
        else:
            return True  # left list is empty


def comparator(left, right):
    if compare_pair_arr(left, right):
        return 1
    return -1


from functools import cmp_to_key

sorted_pairs=sorted(pairs, key=cmp_to_key(comparator),reverse=True)
decoder_key=1
for divider_packet in divider_packets:
    decoder_key*=sorted_pairs.index(divider_packet)+1


print(decoder_key)
