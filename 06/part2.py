f = open("06/input.txt", "r")
input = f.readlines()

trash, time_string = input[0].strip().split(":")
trash, distance_string = input[1].strip().split(":")
time = int(time_string.replace(" ", ""))
record_distance = int(distance_string.replace(" ", ""))

sum = 0
for wind_up_time in range(1, time-1):
    distance = wind_up_time * (time - wind_up_time)
    if distance > record_distance:
        sum += 1
print(sum)

f.close()