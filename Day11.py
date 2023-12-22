import numpy as np
import re

# Define input file name
file_name = "day11data.txt"
expansion_factor = 1000000 - 1

# Get size of map
def map_size(file_n):
    with open(file_n, 'r') as file:
        map = file.readlines()
        file_length = len(map)
        file_width = len(map[0]) - 1
    return file_length, file_width 

# Read file into a 2D array
def create_map(file_n):
    map = np.empty(map_size(file_n), dtype=object)
    with open(file_n, 'r') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                map[i][j] = char
    return map # returns image that is indexed y, x starting from top left = map[0][0]

def find_galaxies(map):
    galaxies = np.where(map == "#")
    return galaxies  # returns y, x

def get_expanded_coords(galaxies, map):
    line_atlas = [i for i in range(0, 140, 1)]
    expanded_y_coords = list(set(line_atlas).difference(set(galaxies[0])))
    expanded_x_coords = list(set(line_atlas).difference(set(galaxies[1])))
    return expanded_y_coords, expanded_x_coords

def between(limit_1, limit_2, pos):
    if limit_1 < pos < limit_2 or limit_2 < pos < limit_1:
        return True
    else:
        return False

def distance(gal_1_y, gal_1_x, gal_2_y, gal_2_x, expanded_y, expanded_x):
    y_dist = abs(gal_1_y - gal_2_y) + expansion_factor*sum(between(gal_1_y, gal_2_y, expansion) for expansion in expanded_y)
    x_dist = abs(gal_1_x - gal_2_x) + expansion_factor*sum(between(gal_1_x, gal_2_x, expansion) for expansion in expanded_x)
    return x_dist + y_dist

# main

map = create_map(file_name)

glxy_locs = np.array([find_galaxies(map)[0], find_galaxies(map)[1]])

expanded_coords = get_expanded_coords(glxy_locs, map)

total_distance = 0
for i in range(len(glxy_locs[0])):
    for j in range(len(glxy_locs[0])):
        if j > i:
            total_distance += distance(glxy_locs[0][i], glxy_locs[1][i], glxy_locs[0][j], glxy_locs[1][j], expanded_coords[0], expanded_coords[1])

print('total_distance: ', total_distance)