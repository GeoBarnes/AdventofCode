import numpy as np
import collections
import re

file_name = "day7data.txt"
SORT_ORDER = {"A": 0, "K": 1, "Q": 2, "T": 3, "9": 4, "8": 5, "7": 6, "6": 7, "5": 8, "4": 9, "3": 10, "2": 11, "J": 12}

# Retrieve hands and rankings from file
def read_file():
    hands = np.empty(shape=(1000, 2), dtype=object)
    with open(file_name,"r") as file:
        for i, line in enumerate(file):
            hands[i] = np.array([s for s in re.findall(r'[A-Z0-9]+', line)], dtype=object)
    return hands

def classify_hand(hand_string):
    count = collections.Counter()
    j_count = hand_string.count('J')
    hand_string_strip = hand_string.replace('J', '')

    # Count the number of instances of each card in hand
    count.update(hand_string_strip)
    hand_sig = []
    for card in set(hand_string_strip):
        hand_sig.append((card, count[card])[1])
        hand_sig.sort(reverse=True)

    if 0 < j_count < 5:
        hand_sig[0] += j_count
    elif j_count == 5:
        hand_sig = [5]
    # Return the type of hand described by the number of matching cards i.e. [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1] or [1,1,1,1,1]
    return hand_sig

def sort_hand_type(hands):
    hands.sort(key=lambda val: [SORT_ORDER[list(val[0])[0]], SORT_ORDER[list(val[0])[1]], SORT_ORDER[list(val[0])[2]], 
                                SORT_ORDER[list(val[0])[3]], SORT_ORDER[list(val[0])[4]]])

def flatten(xss):
    return [x for xs in xss for x in xs]

def calc_score(all_ordered_hands):
    score = 0
    for i, hand in enumerate(all_ordered_hands):
        score += (1000-i)*int(hand[1])
    return score

all_hands = read_file()

five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = [],[],[],[],[],[],[]
all_hands_ordered = []

# Create list of hands of each type
for hand in all_hands:
    hand_type = classify_hand(hand[0])
    if hand_type == [5]:
        five_kind.append(hand)
    if hand_type == [4,1]:
        four_kind.append(hand)
    if hand_type == [3,2]:
        full_house.append(hand)
    if hand_type == [3,1,1]:
        three_kind.append(hand)
    if hand_type == [2,2,1]:
        two_pair.append(hand)
    if hand_type == [2,1,1,1]:
        one_pair.append(hand)
    if hand_type == [1,1,1,1,1]:
        high_card.append(hand)

# Sort inside each type of hand
sort_hand_type(five_kind)
sort_hand_type(four_kind)
sort_hand_type(full_house)
sort_hand_type(three_kind)
sort_hand_type(two_pair)
sort_hand_type(one_pair)
sort_hand_type(high_card)

# Append in correct order to list of all hands
all_hands_ordered.append(five_kind)
all_hands_ordered.append(four_kind)
all_hands_ordered.append(full_house)
all_hands_ordered.append(three_kind)
all_hands_ordered.append(two_pair)
all_hands_ordered.append(one_pair)
all_hands_ordered.append(high_card)

all_hands_ordered_flat = flatten(all_hands_ordered)

total_winnings = calc_score(all_hands_ordered_flat)

print('Part 1 total winnings: ', total_winnings) # = 243101568

