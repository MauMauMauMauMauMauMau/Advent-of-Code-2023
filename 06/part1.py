f = open("06/input.txt", "r")
input = f.readlines()

trash, time_string = input[0].strip().split(":")
trash, distance_string = input[1].strip().split(":")
times = [int(i) for i in time_string.split()]
record_distances = [int(i) for i in distance_string.split()]

product = 1
for time, record_distance in zip(times, record_distances):
    sum = 0
    for wind_up_time in range(1, time-1):
        distance = wind_up_time * (time - wind_up_time)
        if distance > record_distance:
            sum += 1
    product *= sum
print(product)

f.close()