f = open("08/input.txt", "r")
lines = f.readlines()

instructions = lines[0].strip()
names, left_neighbors, right_neighbors = [], [], []
for line in lines[2:]:
    name, neighbors = line.strip().split(" = ")
    left, right = neighbors.strip("()").split(", ")
    names.append(name)
    left_neighbors.append(left)
    right_neighbors.append(right)
nodes = {name: [left, right] for name, left, right in zip(names, left_neighbors, right_neighbors)}

counter = 0
name = "AAA"
while name != "ZZZ":
    instruction = instructions[counter % len(instructions)]
    if instruction == 'L':
        name = nodes[name][0]
    elif instruction == 'R':
        name = nodes[name][1]
    counter += 1
print(counter)

f.close()