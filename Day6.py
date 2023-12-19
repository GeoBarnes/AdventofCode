import math

# Calculate number of ways to beat the record in each race
def num_solutions(time, distance):
    # Find upper and lower bounds
    upper_bound = math.floor((time + math.sqrt(time**2 - 4*(distance+1)))/2)
    lower_bound = math.ceil((time - math.sqrt(time**2 - 4*(distance+1)))/2)
    num_sols = upper_bound - lower_bound + 1
    return num_sols

race_1 = num_solutions(49, 263)
race_2 = num_solutions(97, 1532)
race_3 = num_solutions(94, 1378)
race_4 = num_solutions(94, 1851)

race_5 = num_solutions(49979494, 263153213781851)

# Part 1
print(race_1 * race_2 * race_3 * race_4) # = 4403592 (part 1 answer)

# Part 2
print(race_5) # = 38017587 (part 2 answer)