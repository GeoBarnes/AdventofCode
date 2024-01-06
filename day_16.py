"""Solution to advent of code day 16 part 1 https://adventofcode.com"""

import numpy as np

FILE_NAME = "day_16_data_test.txt"

# Define the directions according to the indexing of the file
N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)


def add_tup(t1, t2):
    """Adds tuples as if they were vectors."""
    if not t1:
        return ()
    return (t1[0] + t2[0],) + add_tup(t1[1:], t2[1:])


def layout_size(file_n):
    """Returns the length and width of the mirror layout."""
    with open(file_n, "r", -1, "UTF-8") as file:
        layout = file.readlines()
        file_length = len(layout)
        file_width = len(layout[0]) - 1
    return file_length, file_width


def create_layout(file_name):
    """Read and return mirror layout as 2d array."""
    layout = np.empty(layout_size(file_name), dtype=object)
    with open(file_name, "r", -1, "UTF-8") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                layout[i][j] = char
    return layout


def get_char(pos, layout):
    """Returns the character at the given position."""
    return layout[pos]


def check_inside(pos):
    """Returns true if position is inside the layout"""
    return (pos[0][0] not in [-1, 10]) and (pos[0][1] not in [-1, 10])


def get_next_pos(pos, direction, layout):
    """Returns the next position(s) of the beam of light."""
    next_pos = add_tup(pos, direction)
    next_char = get_char(add_tup(pos, direction), layout)

    if (direction == E and next_char == "\\") or (direction == W and next_char == "/"):
        return [next_pos, S]
    if (direction == E and next_char == "/") or (direction == W and next_char == "\\"):
        return [next_pos, N]
    if (direction == N and next_char == "\\") or (direction == S and next_char == "/"):
        return [next_pos, W]
    if (direction == N and next_char == "/") or (direction == S and next_char == "\\"):
        return [next_pos, E]
    if direction in [N, S] and next_char == "-":
        return [next_pos, E, W]
    if direction in [E, W] and next_char == "|":
        return [next_pos, N, S]
    return [next_pos, direction]
    # if (
    #    next_char == "."
    #    or (dir in [N, S] and next_char == "|")
    #    or (dir in [E, W] and next_char == "-")
    # ):
    #    return dir


def main():
    """Calulates number of energised tiles in mirror layout."""
    layout = create_layout(FILE_NAME)
    # Record all energised tiles as well as direction moved through
    energised = []
    # Create list of start positions to check along with initial direction
    start_pos = [((0, 0), E)]
    for start in start_pos:
        pos = start
        while True:
            if not check_inside([add_tup(pos[0], pos[1])]):
                break
            next_pos = get_next_pos(pos[0], pos[1], layout)
            # If beam splits add second beam direction to start_pos
            if len(next_pos) == 3 and check_inside([next_pos[0], next_pos[2]]):
                start_pos.append([next_pos[0], next_pos[2]])
            if pos in energised:
                break
            energised.append(pos)
            print("next position: ", next_pos)
            pos = (next_pos[0], next_pos[1])

    # print(energised)
    print(len(set(pos[0] for pos in energised)))  # 116 too low
    print(set(pos[0] for pos in energised))


if __name__ == "__main__":
    main()
