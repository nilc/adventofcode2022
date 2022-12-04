import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import string

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()


def get_set_numbers(a_range):
    s = int(a_range.split("-")[0])
    e = int(a_range.split("-")[1])

    return set(range(s, e + 1))


def get_is_in_both(s1: set, s2: set):
    issubset = s1.issubset(s2)
    if (issubset):
        print(f"{s1} and {s2} subsets eachother")
    return issubset


listofset = []
sum = 0
for line in lines:
    line = line.strip()
    line_split = line.split(",")
    s1 = get_set_numbers(line_split[0])
    s2 = get_set_numbers(line_split[1])
    if (len(s1.intersection(s2)) > 0):
        sum = sum + 1

print(sum)
