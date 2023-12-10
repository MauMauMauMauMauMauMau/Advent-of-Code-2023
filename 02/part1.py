input = open("02/input.txt", "r")
lines = input.readlines()

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

sum = 0
for line in lines:
    game_possible = True

    first_part, last_part = line.split(":")
    id = int(first_part.split(" ")[1].strip())

    tries = last_part.split(";")

    for tri in tries:
        tri.strip()
        balls = tri.split(",")

        for ball in balls:
            amount, color = ball.strip().split(" ")
            amount = int(amount)    
            
            if color == "red" and amount > RED_THRESHOLD: game_possible = False
            if color == "green" and amount > GREEN_THRESHOLD: game_possible = False
            if color == "blue" and amount > BLUE_THRESHOLD: game_possible = False

    if game_possible: sum += id

print(sum)

input.close()