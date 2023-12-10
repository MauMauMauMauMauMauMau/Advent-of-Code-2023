input = open("02/input.txt", "r")
lines = input.readlines()

sum = 0
for line in lines:
    first_part, last_part = line.split(":")
    id = int(first_part.split(" ")[1].strip())

    tries = last_part.split(";")

    min_red = 0
    min_green = 0
    min_blue = 0

    for tri in tries:
        tri.strip()
        balls = tri.split(",")

        for ball in balls:
            amount, color = ball.strip().split(" ")
            amount = int(amount)    

            if color == "red": 
                if amount > min_red: min_red = amount
            
            if color == "green": 
                if amount > min_green: min_green = amount

            if color == "blue": 
                if amount > min_blue: min_blue = amount

    power = min_red * min_green * min_blue
    sum += power

print(sum)

input.close()