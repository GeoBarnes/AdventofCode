import re
import numpy as np
import itertools

# Define input file name
file_name = "day12data.txt"

def read_file(file_n):
    with open(file_n, 'r') as file:
        spring_conditions = []
        spring_groups = []
        for line in file:
            part_1, part_2 = line.split(' ')
            groups = (part_2.strip()).split(',')
            spring_conditions.append(part_1)
            spring_groups.append([int(i) for i in groups])
    return spring_conditions, spring_groups


def missing_breaks(spring_condition, spring_groups):
    total_breaks = sum([i for i in spring_groups])
    known_breaks = spring_condition.count('#')
    return total_breaks - known_breaks


def missing_works(spring_condition, spring_groups):
    missing_springs = spring_condition.count('?')
    return missing_springs - missing_breaks(spring_condition, spring_groups)


def is_match(spring_condition, spring_groups):
    spring_breaks = [s.span()[1] - s.span()[0] for s in re.finditer('[\#]+', spring_condition)]
    if spring_breaks == spring_groups: 
        return True
    return False


# main

# Find the damaged records and damaged spring groups
dmg_res, dmg_groups = read_file(file_name)

total_arrangements = 0

# Loop through the damaged records
for i, row in enumerate(dmg_res):
    arrangements = 0
    dmg_vals = [s.start() for s in re.finditer('\?', row)] 
    for replacements in itertools.combinations(dmg_vals, missing_breaks(row, dmg_groups[i])):
        row_fix = '' + row
        for replacement in replacements:
            row_fix = row_fix[:replacement] + '#' + row_fix[replacement+1:] 
        
        row_fix = row_fix.replace('?', '.')
        arrangements += is_match(row_fix, dmg_groups[i])

    total_arrangements += arrangements

print('Total arrangements: ', total_arrangements)