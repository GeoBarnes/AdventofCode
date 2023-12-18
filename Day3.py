import re

number_locations = []
symbol_locations =[]

# Read line and extract numbers with locations and locations of symbols
def read_line(i, line):
    # Get list of numbers in line
    numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
    # Get the position of the numbers in line
    number_x_coords = [(m.start(0), m.end(0)-1) for m in re.finditer(r'\b\d+\b', line)]
    # Get the position of the symbols in line
    symbol_x_coords = [(m.start(0)) for m in re.finditer(r'[&@#$%*/=+-]', line)]

    # Populate list with [x,y] coords of symbols
    for x_coord in symbol_x_coords:
        symbol_locations.append([x_coord, i])

    # Populate list with [number, [x_start, x_end, y]]
    for j, number in enumerate(numbers):
        number_locations.append([number, [number_x_coords[j][0], number_x_coords[j][1], i]])

   # return number_locations, symbol_locations

def proximity_check(num_coords):
    is_symbol_proximate = False
    for x, y in symbol_locations:
        if abs(y - num_coords[2]) <= 1:
            if x >= num_coords[0] - 1 and x <= num_coords[1] + 1:
                is_symbol_proximate = True
    return is_symbol_proximate

# Open file and process each line
with open("day3data.txt","r") as file:
    for i, line in enumerate(file):
        read_line(i, line)

total = 0
for number in number_locations:
    if proximity_check(number[1]):
        total = total + number[0]

print('Total : ', total)

# Total = 538046 Correct answer