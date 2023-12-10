import numpy as np

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
rank = {card: i for i, card in enumerate(cards)}

def get_hand_type(hand):
    card_occurences = {card: 0 for card in cards}
    for card in hand:
        card_occurences[card] += 1
    if 'J' in hand:
        temp = card_occurences['J']
        card_occurences['J'] = 0
        card_occurences[max(card_occurences, key=card_occurences.get)] += temp
    if any([card_occurences[card] == 5 for card in cards]):
        return 6
    elif any([card_occurences[card] == 4 for card in cards]):
        return 5
    elif any([card_occurences[card] == 3 for card in cards]) and any([card_occurences[card] == 2 for card in cards]):
        return 4
    elif any([card_occurences[card] == 3 for card in cards]) and sum([card_occurences[card] == 1 for card in cards]) == 2:
        return 3
    elif sum([card_occurences[card] == 2 for card in cards]) == 2:
        return 2
    elif sum([card_occurences[card] == 2 for card in cards]) == 1 and sum([card_occurences[card] == 1 for card in cards]) == 3:
        return 1
    elif sum([card_occurences[card] == 1 for card in cards]) == 5:
        return 0
    

def first_higher(hand1, hand2):
    if get_hand_type(hand1) == get_hand_type(hand2):
        for card1, card2 in zip(hand1, hand2):
            if rank[card1] > rank[card2]:
                return True
            elif rank[card1] < rank[card2]:
                return False
        return False
    else:
        if get_hand_type(hand1) > get_hand_type(hand2):
            return True
        else:
            return False


f = open("07/input.txt", "r")
lines = f.readlines()
hands, bids = [], []
for line in lines:
    hand, bid = line.strip().split()
    hands.append(hand)
    bids.append(int(bid))
f.close()

hand_rank = np.ones(len(lines), dtype=int)
for i, hand1 in enumerate(hands):
    for hand2 in hands:
        if first_higher(hand1, hand2):
            hand_rank[i] += 1
print("result =", np.dot(hand_rank, np.array(bids)).sum())