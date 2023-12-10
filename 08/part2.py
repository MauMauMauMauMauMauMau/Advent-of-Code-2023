import numpy as np

f = open("08/input.txt", "r")
lines = f.readlines()

instructions = lines[0].strip()
names, left_neighbors, right_neighbors = [], [], []
starts = []
for line in lines[2:]:
    name, neighbors = line.strip().split(" = ")
    left, right = neighbors.strip("()").split(", ")
    names.append(name)
    left_neighbors.append(left)
    right_neighbors.append(right)
    if name[2] == 'A':
        starts.append(name)
nodes = {name: [left, right] for name, left, right in zip(names, left_neighbors, right_neighbors)}

periods = []
for start in starts:
    possible_end_counters = []
    counter = 0
    current = start
    while counter < 100000:
        # falls auf möglicher Endnode (endet auf Z), counter merken
        if current[2] == 'Z':
            possible_end_counters.append(counter)
        
        # go to next node
        instruction = instructions[counter % len(instructions)]
        if instruction == 'L':
            current = nodes[current][0]
        elif instruction == 'R':
            current = nodes[current][1]
        counter += 1
    
    # find period
    period = possible_end_counters[-1] - possible_end_counters[-2]
    periods.append(period)
    print("Startnode:", start, "->", possible_end_counters, "period =", period)
print("periods =", periods)
print("lcm =", np.lcm.reduce(np.array(periods).astype(np.int64)))

f.close()