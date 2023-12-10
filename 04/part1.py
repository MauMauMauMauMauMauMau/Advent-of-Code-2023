input = open("04/input.txt", "r")
lines = input.readlines()


def hits_to_points(hits):
    if hits == 0: return 0
    if hits == 1: return 1
    if hits > 1: return 2**(hits -1) 


sum = 0
for line in lines:
    trash, numbers = line.strip().split(": ")
    winning, mine = numbers.split(" | ")
    winning_numbers = winning.split()
    my_numbers = mine.split()
    
    hits = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            hits += 1
    
    sum += hits_to_points(hits)

print(sum)

input.close()