import numpy as np

f = open("09/input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
    values = np.array(line.strip().split(), dtype=int)
    value_history = [values]
    while any([value != 0 for value in values]):
        values = values[1:] - values[:-1]
        value_history.append(values)
    for array in value_history:
        sum += array[-1]
print(sum)
f.close()