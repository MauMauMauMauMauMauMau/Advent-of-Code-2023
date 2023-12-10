import numpy as np
sum = 0
for line in open("09/input.txt", "r").readlines():
    values = np.array(line.strip().split(), dtype=int)
    value_history = [values]
    while any([value != 0 for value in values]):
        values = values[1:] - values[:-1]
        value_history.append(values)
    temp_sum = 0
    for array in value_history[::-1]: temp_sum = array[0] - temp_sum
    sum += temp_sum
print(sum)