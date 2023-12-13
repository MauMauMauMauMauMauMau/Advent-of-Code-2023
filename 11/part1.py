# parse data
f = open("11/input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
galaxy_coords = []
lines_wo_galaxies = []
columns_wo_galaxies = []
for y, line in enumerate(lines):
    x = 0
    if line.find('#') == -1:
        lines_wo_galaxies.append(y)
    else:
        while x < len(line):
            x = line.find('#', x)
            if x == -1: break
            galaxy_coords.append([x, y])
            x += 1
columns = ["".join([lines[y][x] for y in range(len(lines))]) for x in range(len(lines[0]))]
for x, column in enumerate(columns):
    if column.find('#') == -1: columns_wo_galaxies.append(x)
f.close()

# work with data
sum = 0
for i, galaxy1 in enumerate(galaxy_coords):
    for galaxy2 in galaxy_coords[i + 1:]:
        x1, y1 = galaxy1
        x2, y2 = galaxy2
        sum += abs(x2 - x1) + abs(y2 - y1)
        for x in range(min(x1, x2), max(x1, x2)):
            if x in columns_wo_galaxies: sum += 1000000 - 1
        for y in range(min(y1, y2), max(y1, y2)):
            if y in lines_wo_galaxies: sum += 1000000 - 1
print(sum)