import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import string

from collections import defaultdict

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()


def x_y_format(x, y):
    return (f"{x},{y}")


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight


max_y = len(lines)
max_x = len(lines[0].strip())
heightmap = {}
for y in range(max_y):
    line = lines[y]
    line = line.strip()
    for x in range(max_x):
        char = line[x]
        if char.islower():
            heightmap[x_y_format(x, y)] = string.ascii_lowercase.index(char)
        else:
            heightmap[x_y_format(x, y)] = char


def get_edges(x, y, heightmap):
    right = x_y_format(x + 1, y)
    left = x_y_format(x - 1, y)
    up = x_y_format(x, y - 1)
    down = x_y_format(x, y + 1)
    edges = []
    start_pos = x_y_format(x, y)
    startvalue = get_height(start_pos, heightmap)
    for dir in [right, left, down, up]:
        height = get_height(dir, heightmap)
        if height is not None and height <= startvalue + 1:
            edges.append([start_pos, dir, 1])
    return edges


def get_height(dir, heightmap):
    value = heightmap.get(dir)
    if value == "S":
        return string.ascii_lowercase.index("a")
    elif value == "E":
        return string.ascii_lowercase.index("z")
    return value


edges = []
startpos = None
endpos = None
for y in range(max_y):
    for x in range(max_x):
        edges += get_edges(x, y, heightmap)
        if heightmap[x_y_format(x, y)] == "S":
            startpos = x_y_format(x, y)
        if heightmap[x_y_format(x, y)] == "E":
            endpos = x_y_format(x, y)
graph = Graph()
for e in edges:
    graph.add_edge(e[0], e[1], e[2])


def dijsktra(graph, initial, end, shortest_paths_weigth=None):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight and (shortest_paths_weigth is None or shortest_paths_weigth > weight):
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return None
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


def solution_part1():
    solution = dijsktra(graph, startpos, endpos)
    print(solution)
    print(len(solution) - 1)


solution_part1()

lowest = 999999
for key in heightmap:
    if get_height(key, heightmap) == 0:
        s = dijsktra(graph, key, endpos, lowest)
        if s:
            a_path = len(s)
            if a_path < lowest:
                print(f"found new shortest path {a_path}: {s} ")
                lowest = a_path
print(lowest-1)
