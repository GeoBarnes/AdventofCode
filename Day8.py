import re

file_name = "day8data.txt"

directions = "LRRRLRRLLLRRRLRLRRLRRRLRLRRRLLLRRLRRLRRRLRRRLRLLRLRRLRRLLRRLRLRRRLRRLRRLRRLLRRRLRLRLRLRLLRRLLLRRLRLRRLRLLLLRRLRRRLRRLRRRLLRRRLRRLRRRLRLLRLRRLRRLLRRRLLLRLRRRLLLRRLLRRRLLRRLRRLRRLRLRRRLLRRRLRLLRLRRLLRLRRLRLLRLRRLRRRLLRRLLRRRLRRLRLRLRRRLRLRRRLRRRLRRLRRRLRLLRRRLLRRRR"

# Read map information from file
# Create a left dictionary and a right dictionary from the map
def map_dics():
    left_map = {}
    right_map= {}
    with open(file_name,"r") as file:
        for line in file:
            coords = [s for s in re.findall(r'[A-Z]+', line)]
            left_map[coords[0]] = coords[1]
            right_map[coords[0]] = coords[2]
    return left_map, right_map

def follow_directions(directions, left_map, right_map):
    pos = 'AAA'
    end = 'ZZZ'
    steps = 0
    while True:
        for char in directions:
            if pos == end:
                return steps
            steps += 1
            if char == 'L':
                pos = left_map[pos]
            elif char == 'R':
                pos = right_map[pos]

# Create dictionaries
left_map, right_map = map_dics()

# Follow directions using maps
print(follow_directions(directions, left_map, right_map)) # = 17621 (part 1)

