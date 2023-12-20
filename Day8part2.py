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
            #coords = [s for s in re.findall(r'[0-9A-Z][0-9A-Z][A-Z]', line)]
            left_map[coords[0]] = coords[1]
            right_map[coords[0]] = coords[2]
    return left_map, right_map

def find_start_pos(map):
    start_pos = []
    for key in map:
        pattern = re.compile("..A")
        if pattern.match(key):
            start_pos.append(key)
    return start_pos

def end_check(positions):
    is_end = True
    pattern = re.compile("..Z")
    for pos in positions:
        if not pattern.match(pos):
            is_end = False 
    return is_end

def follow_directions(directions, left_map, right_map):
    pos_s = find_start_pos(left_map)
    num_pos = len(pos_s)
    print('starts: ', pos_s)
    steps = 0
    #while True:
    while steps < 100000000:
        for char in directions:
            #print('positions: ', pos_s)
            if end_check(pos_s):
                return steps
            else:
                steps += 1
            for i in range(num_pos):
                if char == 'L':
                    pos_s[i] = left_map[pos_s[i]]
                elif char == 'R':
                    pos_s[i] = right_map[pos_s[i]]

# Create dictionaries
left_map, right_map = map_dics()

# Follow directions using maps
print('Number of steps: ', follow_directions(directions, left_map, right_map)) # = 17621 (part 1)

