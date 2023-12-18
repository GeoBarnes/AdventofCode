import re
import math
import copy

# Calculate the score for each line of the file
def card_score(line):
    # Remove the card number part of the line
    parts_1_2 = line.split(':')[1]
    # Create a list of the winning numbers and a list of the numbers that I have
    part_1, part_2 = parts_1_2.split('|')
    winning_numbers = [int(s) for s in re.findall(r'\b\d+\b', part_1)]
    my_numbers = [int(s) for s in re.findall(r'\b\d+\b', part_2)]
    # Find count of my numbers that appear in the winning numbers
    matches = len(set(my_numbers).intersection(set(winning_numbers)))
    # This is the score for the line (for part 1 of the problem)
    #score = math.floor(2**(matches)/2)
    return matches

card_wins = []
total_games = []
with open("day4data.txt","r") as file:
    for i, line in enumerate(file):
        card_wins.append([i+1, card_score(line)])
        total_games.append([i+1, 1])

# Calculate total number of games
for i in range(0, len(card_wins)):
    if card_wins[i][1] > 0:
        for j in range(1, card_wins[i][1]+1): 
            total_games[i+j][1] = total_games[i+j][1] + total_games[i][1]

print('Total games: ', sum(y for x,y in total_games))

# Total games = 13114317
