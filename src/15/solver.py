import dataclasses
import json
import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import re

from collections.abc import Sequence
from copy import deepcopy

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

rockpaths = {}
search_area = 4000000


@dataclasses.dataclass
class beacon():
    x_from_sensor: int
    y_from_sensor: int


@dataclasses.dataclass(frozen=True, eq=True)
class pos():
    x: int
    y: int


@dataclasses.dataclass
class sensor():
    x: int
    y: int
    beacons = []
    my_manhattan_distance = None
    my_cover_points: set = None

    def covers_range(self, x, y):
        end_y = self.y + self.my_manhattan_distance
        start_y = self.y - self.my_manhattan_distance
        if start_y <= y <= end_y:
            startx, endx = self.getxrange(y)
            if startx <= x <= endx:
                return endx
        return False

    def getxrange(self, y):
        width_on_each_side = (self.my_manhattan_distance - abs(self.y - y))
        startx = self.x - width_on_each_side
        endx = self.x + width_on_each_side
        return startx, endx

    def coversfrom(self):
        return [pos(self.x - self.my_manhattan_distance, self.y - self.my_manhattan_distance)
            , pos(self.x + self.my_manhattan_distance, self.y + self.my_manhattan_distance)]

    def is_in_my_range(self, pos):
        range_to_see = self.manhattan_distance(pos)
        if (self.my_manhattan_distance >= range_to_see):
            return True
        return False

    def manhattan_distance(self, pos):
        return abs(self.x - pos.x) + abs(self.y - pos.y)

    def add_beacon(self, a_beacon):
        self.closestbeacon_pos = pos(x=a_beacon.x_from_sensor, y=a_beacon.y_from_sensor)
        self.my_manhattan_distance = self.manhattan_distance(self.closestbeacon_pos)
        self.beacons.append(a_beacon)


def flatten(l):
    return [item for sublist in l for item in sublist]


rockpaths = {}


####B######################
def anything_on_pos(x, y):
    return y in rockpaths and x in rockpaths[y]


def print_state():
    maxx, minx, rockpaths = get_map_data()
    for y in range(min(rockpaths.keys()), max(rockpaths.keys()) + 1):
        line = f"{y} "
        for x in range(minx, maxx + 1):
            if anything_on_pos(x, y):
                line += rockpaths[y][x]
            elif pos(x, y) in allcovered:
                line += "#"
            else:
                line += "."
        print(line)


def get_map_data():
    rockpaths = create_map()

    def flatten(l):
        return [item for sublist in l for item in sublist]

    m = map(lambda s: s.coversfrom()[0].x, sensors)
    minx = min(m)
    maxx = max(map(lambda s: s.coversfrom()[1].x, sensors))
    return maxx, minx, rockpaths


def create_map():
    rockpaths = {}
    for sensor in sensors:
        if (sensor.y not in rockpaths):
            rockpaths[sensor.y] = {}
        rockpaths[sensor.y][sensor.x] = "S"
        if (sensor.closestbeacon_pos.y) not in rockpaths:
            rockpaths[sensor.closestbeacon_pos.y] = {}
        rockpaths[sensor.closestbeacon_pos.y][sensor.closestbeacon_pos.x] = "B"
    return rockpaths


def parse(line):
    pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    matches = re.finditer(pattern, line)
    data = []
    for match in matches:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(match.group(i)) for i in range(1, 5)]
    a_sensor = sensor(x=sensor_x, y=sensor_y)
    a_beacon = beacon(x_from_sensor=beacon_x, y_from_sensor=beacon_y)
    a_sensor.add_beacon(a_beacon)
    return a_sensor


sensors: [sensor] = []

for line in lines:
    sensors.append(parse(line))

allcovered = set()
print(f"number of sensors{len(sensors)}")


def solve_part2():
    # print_state()
    foundvalue = False

    for y in range(0, search_area + 1):
        if (foundvalue):
            break
        if y % 10000 == 0:
            print(f"searching {y}")
        x = 0
        while x < search_area + 1:
            sensors_max_x = map(lambda asensor: asensor.covers_range(x, y), sensors)
            xs = list(filter(lambda value: value != False, sensors_max_x))
            if len(xs) == 0:
                print(f"{x},{y} correct answer:{x * search_area + y}")
                foundvalue = True
                break
            x = max(x + 1, max(xs))


solve_part2()


def solve_part1():
    global rockpaths, line
    # print_state()
    test_y = 2000000
    maxx, minx, rockpaths = get_map_data()
    possible_beacon_pos = set()
    line = ""
    for test_x in (range(minx - 1, maxx + 1)):
        test_pos = pos(test_x, test_y)
        is_covered = False
        if (anything_on_pos(test_pos.x, test_pos.y)):
            is_covered = True
        what_is_here = rockpaths[test_pos.y][test_pos.x]
        line += what_is_here
        if (what_is_here == "B"):
            is_covered = False
        else:
            for s in sensors:
                if s.is_in_my_range(test_pos):
                    is_covered = True
                    break
                if (is_covered):
                    # line += "#"
                    # print(f"{test_pos} is covered")
                    possible_beacon_pos.add(f"{test_pos.x},{test_pos.y}")
    print(len(possible_beacon_pos))

# solve_part1()
