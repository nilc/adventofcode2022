import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import string

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()


def get_prio(l):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return alphabet.index(l) + 1


def get_is_in_both(s1: [], s2: []):
    return set(s1).intersection(set(s2))


def get_is_in_all(s1: [], s2: [], s3: []):
    return set(s1).intersection(set(s2)).intersection(set(s3))


linesofthree = []

sum = 0
for line in lines:
    line = line.strip()
    linesofthree.append(line)
    if len(linesofthree) == 3:
        in_all = get_is_in_all(linesofthree[0], linesofthree[1], linesofthree[2])
        print(in_all)
        for l in in_all:
            sum = sum + get_prio(l)
        linesofthree = []

print(sum)
