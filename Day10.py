import numpy as np

# Define input file name
file_name = "day10data.txt"

# Define the directions according to the indexing of the file
north = (-1, 0)
east = (0, 1)
south = (1, 0)
west = (0, -1)

directions = [north, east, south, west]

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
    return map # returns map that is indexed y, x starting from top left = map[0][0]

# Find the index of the "S" on the map
def find_start(map):
    start_loc = np.where(map == "S")
    return start_loc[0][0], start_loc[1][0]  # returns y, x

# Return the symbol at the location given
def get_symb(pos, map):
    return map[pos]

# Check whether a valid link exists between two map positions 
def check_link_valid(pos, next_pos, map):
    symb = get_symb(pos, map)
    # Handle edges of the map by replacing outside edge points with "."
    try:
        next_symb = get_symb(next_pos, map)
    except:
        next_symb = "."
    direction = (next_pos[0] - pos[0], next_pos[1] - pos[1])
    if any(symb in dir for dir in ["|", "L", "J"]) and any(next_symb in dir for dir in ["|", "7", "F", "S"]) and direction == north:
        return True
    elif any(symb in dir for dir in ["-", "L", "F", "S"]) and any(next_symb in dir for dir in ["-", "J", "7"]) and direction == east:
        return True
    elif any(symb in dir for dir in ["|", "7", "F", "S"]) and any(next_symb in dir for dir in ["|", "L", "J"]) and direction == south:
        return True
    elif any(symb in dir for dir in ["-", "J", "7"]) and any(next_symb in dir for dir in ["-", "L", "F", "S"]) and direction == west:
        return True
    else:
        return False

def get_next_pos(prev_pos, pos, map):
    y, x = pos[0], pos[1]
    current_symb = get_symb(pos, map)
    for next_pos_try in [(y-1,x), (y,x+1), (y+1,x), (y,x-1)]: # (N,E,S,W)
        if next_pos_try != prev_pos and check_link_valid(pos, next_pos_try, map):
            return next_pos_try

def get_bulk_coords(loop_coords, map):
    atlas = [(i, j) for i in range(0, 140, 1) for j in range (0, 140, 1)]
    bulk_coords = list(set(atlas).difference(set(loop_coords)))
    return bulk_coords

# Should account for 'S' = 'F' but apparently doesn't matter
def calc_area(loop_coords, map):
    # Find all coordinates that do not make up the loop
    bulk_coords = get_bulk_coords(loop_coords, map)
    area_count = 0
    for pos in bulk_coords:
        loop_crossings_count = 0
        # Check each point on the loop to the direct east of the position
        for boundary_point in loop_coords:
            if boundary_point[0] == pos[0] and boundary_point[1] > pos[1]:
                if get_symb(boundary_point, map) == '|':
                    loop_crossings_count += 1
                if get_symb(boundary_point, map) == 'F':
                    eastward_jump = 1
                    while get_symb((boundary_point[0], boundary_point[1]+eastward_jump), map) == '-':
                        eastward_jump += 1
                    if get_symb((boundary_point[0], boundary_point[1]+eastward_jump), map) == 'J':
                        loop_crossings_count += 1
                if get_symb(boundary_point, map) == 'L':
                    eastward_jump = 1
                    while get_symb((boundary_point[0], boundary_point[1]+eastward_jump), map) == '-':
                        eastward_jump += 1
                    if get_symb((boundary_point[0], boundary_point[1]+eastward_jump), map) == '7':
                        loop_crossings_count += 1
                #print(boundary_point)
        if loop_crossings_count % 2 == 1:
            area_count += 1
    return area_count        

# main

# Create map from file
map = create_map(file_name)
# Set starting position
curr_pos = find_start(map)
# Move 1 step to get off the start (take any dummy position as previous and will move to first valid found from N,E,S,W)
prev_pos = curr_pos
curr_pos = get_next_pos((0,0), curr_pos, map)
step_count = 1
loop_coords = []
while get_symb(curr_pos, map) != "S":
    loop_coords.append(curr_pos)
    old_curr_pos = curr_pos
    curr_pos = get_next_pos(prev_pos, curr_pos, map)
    prev_pos = old_curr_pos
    step_count += 1

print("Furthest point from start: ", step_count/2) # = 6864 part 1

print('Area inside loop: ', calc_area(loop_coords, map))