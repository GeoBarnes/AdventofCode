"""Solution to advent of code day 17 part 1 https://adventofcode.com"""
from collections import defaultdict
import math
import numpy as np

# Define input file name
FILE_NAME = "day_17_data.txt"


def add_tup(t1, t2):
    """Adds tuples as if they were vectors."""
    if not t1:
        return ()
    return (t1[0] + t2[0],) + add_tup(t1[1:], t2[1:])


def map_size():
    """Calculate the size of the map in the file."""
    with open(FILE_NAME, "r", -1, "UTF-8") as file:
        layout = file.readlines()
        file_length = len(layout)
        file_width = len(layout[0]) - 1
    return file_length, file_width


def pos_label(pos, row_length):
    """Returns the integer label of a (y, x) position."""
    return pos[0] * row_length + pos[1] + 1


def label_pos(label, row_length):
    """Returns the (y, x) position of an integer label."""
    return math.floor((label - 1) / row_length), (label - 1) % row_length


def create_layout():
    """Reads heat map from the file and returns 2d array."""
    layout = np.empty(map_size(), dtype=object)
    with open(FILE_NAME, "r", -1, "UTF-8") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                layout[i][j] = int(char)
    return layout


def build_graph():
    """Build graph of connections"""
    # Number points in the file increasing from left to right, top to bottom
    # i.e. 123
    #      456

    edges = []
    row_length = map_size()[0]

    # Create list of all edges in graph
    for n in range(1, row_length**2):
        if n % row_length != 0:
            edges.append([n, n + 1])
        if n <= row_length * (row_length - 1):
            edges.append([n, n + row_length])

    graph = defaultdict(list)

    # Loop over every edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Create the graph as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


# This works but does not restrict to paths of maximum 3 length straight
def dijkstra_shortest_path(graph, layout):
    """Find the shortest path between the start and end points (Dijkstra's algorithm)."""
    row_length = map_size()[0]
    dist = np.empty(row_length**2, dtype=object)
    # Set all but the source points distance to inf
    dist[0] = 0
    for i in range(1, row_length**2):
        dist[i] = np.inf
    q = list(graph)

    while q:
        # Set v vertex with minimum distance in q
        v = min(q, key=lambda x: dist[x - 1])
        q.remove(v)

        # For each neighbour of v update shortest distance if going through v is shorter
        for u in graph[v]:
            if u in q:
                alt = dist[v - 1] + layout[label_pos(v, row_length)]
                dist[u - 1] = min(dist[u - 1], alt)

    print(dist)


def main():
    """Calculates the shortest path from top left to bottom right"""
    layout = create_layout()
    graph = build_graph()

    dijkstra_shortest_path(graph, layout)


if __name__ == "__main__":
    main()
