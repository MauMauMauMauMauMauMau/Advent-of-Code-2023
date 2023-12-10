dir_to_coords = {"north": [0, -1], "east": [1, 0], "south": [0, 1], "west": [-1, 0]}


def find_start(lines):
    for y, line in enumerate(lines):
        x = line.find('S')
        if x != -1: break
    return [x, y]


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
        new_coordinates = [current_coordinates[0] + dir_to_coords[direction][0], current_coordinates[1] + dir_to_coords[direction][1]]
        if direction == "north" and lines[new_coordinates[1]][new_coordinates[0]] in ['|', '7', 'F', 'S']:
            return new_coordinates, "south"
        elif direction == "east" and lines[new_coordinates[1]][new_coordinates[0]] in ['-', 'J', '7', 'S']:
            return new_coordinates, "west"
        elif direction == "south" and lines[new_coordinates[1]][new_coordinates[0]] in ['|', 'L', 'J', 'S']: 
            return new_coordinates, "north"
        elif direction == "west" and lines[new_coordinates[1]][new_coordinates[0]] in ['-', 'L', 'F', 'S']: 
            return new_coordinates, "east"


def is_in_enclosed_area(coords, path, map):
    #print("checking if", coords, "is in area...")
    ray = map[coords[1]][coords[0]:]
    
    # find edges in rays
    #print("  finding all edges...")
    edges = []
    i = 0
    while i < len(ray):
        #print("    finding an edge...")
        edge = []
        if [coords[0] + i, coords[1]] in path:
            while [coords[0] + i, coords[1]] in path:
                edge.append(map[coords[1]][coords[0] + i])
                if map[coords[1]][coords[0] + i] in ['J', '7', '|']: break
                i += 1
            edges.append(edge)
            #print("    found one edge:", edge)
        i += 1
    #print("  found all edges:", edges)
            
    # count applicable edges
    edge_crossings = 0
    for edge in edges:
        if len(edge) == 1:
            edge_crossings += 1
        else:
            if edge[0] == 'F' and edge[-1] == 'J' or edge[0] == 'L' and edge[-1] == '7':
                edge_crossings += 1
    #print("  counted", edge_crossings, "edge crossing")

    if edge_crossings % 2 == 0: return False
    else: return True


# find start and path
f = open("10/input.txt", "r")
lines = f.readlines()
start = find_start(lines)
path = [start]
current = start
prev_dir = None
while True:
    current, prev_dir = next_coordinates(current, prev_dir)
    if current == start:
        break
    path.append(current)
f.close()

# replace S with its correct tube
north_of_start = [start[0] + dir_to_coords["north"][0], start[1] + dir_to_coords["north"][1]]
east_of_start = [start[0] + dir_to_coords["east"][0], start[1] + dir_to_coords["east"][1]]
south_of_start = [start[0] + dir_to_coords["south"][0], start[1] + dir_to_coords["south"][1]]
west_of_start = [start[0] + dir_to_coords["west"][0], start[1] + dir_to_coords["west"][1]]
north_applicable = north_of_start in path and lines[north_of_start[1]][north_of_start[0]] in ['|', '7', 'F']
south_applicable = south_of_start in path and lines[south_of_start[1]][south_of_start[0]] in ['|', 'J', 'L']
east_applicable = east_of_start in path and lines[east_of_start[1]][east_of_start[0]] in ['-', 'J', '7']
west_applicable = west_of_start in path and lines[west_of_start[1]][west_of_start[0]] in ['-', 'F', 'L']
if north_applicable and south_applicable:
    lines[start[1]] = lines[start[1]].replace('S', '|')
elif north_applicable and east_applicable:
    lines[start[1]] = lines[start[1]].replace('S', 'L')
elif north_applicable and west_applicable:
    lines[start[1]] = lines[start[1]].replace('S', 'J')
elif west_applicable and east_applicable:
    lines[start[1]] = lines[start[1]].replace('S', '-')
elif west_applicable and south_applicable:
    lines[start[1]] = lines[start[1]].replace('S', '7')
elif south_applicable and east_applicable:
    lines[start[1]] = lines[start[1]].replace('S', 'F')

# find area
area = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if [x, y] not in path:
            if is_in_enclosed_area([x, y], path, lines):
                area += 1
    print("{:.2f} percent done".format(100*(y+1)/len(lines)))
print("area =", area)