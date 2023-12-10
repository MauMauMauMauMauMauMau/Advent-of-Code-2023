import numpy as np

input = open("04/input.txt", "r")
lines = input.readlines()

hitss = []
for line in lines:
    card, numbers = line.strip().split(": ")
    winning, mine = numbers.split(" | ")
    winning_numbers = winning.split()
    my_numbers = mine.split()
    
    hits = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            hits += 1
    
    hitss.append(hits)


amounts = np.zeros(len(lines))
def add_scratchcard(id):
    amounts[id] += 1
    hits = hitss[id]
    for id_ in range(id + 1, id + hits + 1):
        if id_ < len(lines):
            hits_ = hitss[id_]
            add_scratchcard(id_)
    
    return amounts

for id, hits in enumerate(hitss):
    add_scratchcard(id)

print(amounts.sum().astype(int))

input.close()