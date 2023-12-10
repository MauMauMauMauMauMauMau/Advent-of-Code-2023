import numpy as np

dir_to_coords = {"north": np.array([0, -1]), "east": np.array([1, 0]), "south": np.array([0, 1]), "west": np.array([-1, 0])}


def find_start(lines):
    for y, line in enumerate(lines):
        x = line.find('S')
        if x != -1: break
    return np.array([x, y])


def next_coordinates(current_coordinates, previous_direction):
    current_pipe = lines[current_coordinates[1]][current_coordinates[0]]
    if current_pipe == 'S': possible_directions = {"north", "east", "south", "west"}
    elif current_pipe == '|': possible_directions = {"north", "south"}
    elif current_pipe == '-': possible_directions = {"east", "west"}
    elif current_pipe == 'L': possible_directions = {"north", "east"}
    elif current_pipe == 'J': possible_directions = {"north", "west"}
    elif current_pipe == '7': possible_directions = {"west", "south"}
    elif current_pipe == 'F': possible_directions = {"east", "south"}
    possible_directions -= {previous_direction}
    for direction in possible_directions:
        new_coordinates = current_coordinates + dir_to_coords[direction]
        if direction == "north" and lines[new_coordinates[1]][new_coordinates[0]] in ['|', '7', 'F', 'S']:
            return new_coordinates, "south"
        elif direction == "east" and lines[new_coordinates[1]][new_coordinates[0]] in ['-', 'J', '7', 'S']:
            return new_coordinates, "west"
        elif direction == "south" and lines[new_coordinates[1]][new_coordinates[0]] in ['|', 'L', 'J', 'S']: 
            return new_coordinates, "north"
        elif direction == "west" and lines[new_coordinates[1]][new_coordinates[0]] in ['-', 'L', 'F', 'S']: 
            return new_coordinates, "east"


f = open("10/input.txt", "r")
lines = f.readlines()
start = find_start(lines)
path = [start]
current = start
prev_dir = None
while True:
    current, prev_dir = next_coordinates(current, prev_dir)
    if (current == start).all():
        break
    path.append(current)
print(int(len(path)/2))
f.close()