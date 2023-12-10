f = open("05/input.txt", "r")
input = f.read()


def map_number(x, dest_range_starts, source_range_starts, lengths):
    for dest_range_start, source_range_start, length in zip(dest_range_starts, source_range_starts, lengths):
        if x in range(source_range_start, source_range_start+length):
            return dest_range_start + x - source_range_start
    return x


# parse data
inputs = input.split("\n\n")
seeds = [int(x) for x in inputs[0].split(": ")[1].split()]
maps = []
for block in inputs[1:]:
    name, values = block.split(":\n")
    lines = values.split("\n")
    dest_range_starts, source_range_starts, lengths = [], [], []
    for line in lines:
        dest_range_start, source_range_start, length = line.split()
        dest_range_starts.append(int(dest_range_start))
        source_range_starts.append(int(source_range_start))
        lengths.append(int(length))
    maps.append([dest_range_starts, source_range_starts, lengths])

# use data
location_numbers = []
for seed in seeds:
    x = seed
    for map in maps:
        x = map_number(x, map[0], map[1], map[2])
    location_numbers.append(x)
print(min(location_numbers))

f.close()