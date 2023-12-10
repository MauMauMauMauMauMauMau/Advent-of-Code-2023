input = open("03/input.txt", "r")
lines = input.readlines()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '/', '&', '+', '#', '%', '=', '-', '@', '$']

x_max = len(lines[0]) - 1
y_max = len(lines) - 1

# adjacency matrices
inner_am = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
top_am = [(dx, dy) for dx in (-1, 0, 1) for dy in (0, 1)]
bottom_am = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0)]
left_am = [(dx, dy) for dx in (0, 1) for dy in (-1, 0, 1)]
right_am = [(dx, dy) for dx in (-1, 0) for dy in (-1, 0, 1)]
topright_am = [(dx, dy) for dx in (-1, 0) for dy in (0, 1)]
topleft_am = [(dx, dy) for dx in (0, 1) for dy in (0, 1)]
bottomright_am = [(dx, dy) for dx in (-1, 0) for dy in (-1, 0)]
bottomleft_am = [(dx, dy) for dx in (0, 1) for dy in (-1, 0)]

def adjacency(x, y, adjacency_matrix):
    """Finds all adjacent digits and returns their coordinates in a list. The adjacency condition is given by the adjacency matrix."""
    adj_coords = []
    for (dx, dy) in adjacency_matrix:
        if lines[y + dy][x + dx] in digits:
            adj_coords.append((x + dx, y + dy))
    
    return adj_coords


def adjacent_digit_coords(x, y):
    """Return all adjacent digits' coordinates in a list. Takes care of edge cases."""
    if y == 0: # top
        if x == 0: # top left
            return adjacency(x, y, topleft_am)
        elif x == x_max: # top right
            return adjacency(x, y, topright_am)
        else:
            return adjacency(x, y, top_am)
    elif y == x_max: # bottom
        if x == 0: # bottom left
            return adjacency(x, y, bottomleft_am)
        elif x == x_max: # bottom right
            adjacency(x, y, bottomright_am)
        else: # bottom
            return adjacency(x, y, bottom_am)
    else: # inner
        return adjacency(x, y, inner_am)


def full_number_coords(x, y):
    left, right = 0, 0
    
    dx = 0
    while lines[y][x + dx] in digits: dx += 1
    right = dx - 1

    dx = 0
    while lines[y][x + dx] in digits: dx -= 1
    left = dx + 1
    
    return [(x + Dx, y) for Dx in range(left, right + 1)]


def coords_to_number(coords):
    return int("".join([lines[y][x] for (x, y) in coords]))


symbol_coords = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in symbols:
            symbol_coords.append((x, y))

numbers_coords = []
for (x, y) in symbol_coords:
    adj_digits_coords = adjacent_digit_coords(x, y)

    for (dig_x, dig_y) in adj_digits_coords:
        numbers_coords.append(full_number_coords(dig_x, dig_y))
    
# make numbers_coords unique
temp = set(tuple(tuple(inner) for inner in outer) for outer in numbers_coords)
unique_numbers_coords = [list(inner) for inner in temp]

sum = 0
for coords in unique_numbers_coords:
    sum += coords_to_number(coords) 

print(sum)

input.close()