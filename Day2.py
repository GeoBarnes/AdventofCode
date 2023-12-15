import numpy as np

cube_limits = [14, 13, 12]

def extract_games(line):
    # Strip off the game number and colon
    games = line.split(':')
    games = games[1].split(';')
    
    # Record each games score in order Blue, Green, Red
    game_score = []
    for game in games:
        score_string = game.split(',')
        # Set scores for each colour based on the score string of each round
        scores = [0,0,0]
        for score in score_string:
            score = score.strip()
            if 'blue' in score:
                val = score.split(' ')
                scores[0] = int(val[0])
            if 'green' in score:
                val = score.split(' ')
                scores[1] = int(val[0])
            if 'red' in score:
                val = score.split(' ')
                scores[2] = int(val[0])

        game_score.append(scores)

    return [game_score]

# Check if any round in a given game contains too many of one colour cube, if so then it is not legal
def is_game_legal(game_scores):
    is_game_legal = True
    for round in game_scores:
        if round[0] > cube_limits[0] or round[1] > cube_limits[1] or round[2] > cube_limits[2]:
            is_game_legal = False
            break
    return is_game_legal


def game_power(game_scores):
    max_blue = max([round[0] for round in game_scores])
    max_green = max([round[1] for round in game_scores])
    max_red = max([round[2] for round in game_scores])
    return max_blue*max_green*max_red

# Begin by breaking the line into separate strings for each game
file=open("day2data.txt","r")

# Record scores for all round of all games along with the game number
all_scores = []
game_number = 1
for line in file:
    all_scores.append([game_number, extract_games(line)])
    game_number = game_number + 1

total = 0
total_game_power = 0
for game in all_scores:
    total_game_power = total_game_power + game_power(game[1][0])
    if is_game_legal(game[1][0]):
        total = total + game[0]

print(total)
print(total_game_power)



file.close()