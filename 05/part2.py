class Map:
    def __init__(self, dest_start, source_start, length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.length = length


    def __str__(self):
        return "Map with dest_start = " + str(self.dest_start) + ", source_start =" + str(self.source_start) + ", length = " + str(self.length) 


class Ranges:
    def __init__(self, initials, lengths):
        self.initials = initials
        self.lengths = lengths


    def __str__(self):
        output = "Range with"
        for initial, length in zip(self.initials, self.lengths):
            output += "\n start = " + str(initial) + ", length = " + str(length)
        return output
    

    def min(self):
        return min(self.initials)


def merge_ranges(list_ranges):
    new_initials, new_lengths = [], []
    for ranges in list_ranges:
        new_initials.extend(ranges.initials)
        new_lengths.extend(ranges.lengths)
    return Ranges(new_initials, new_lengths)


def map_ranges(ranges, map):
    mapped_initials, mapped_lengths = [], []
    unmapped_initials, unmapped_lengths = [], []
    for initial, length in zip(ranges.initials, ranges.lengths):
        left_offset = map.source_start - initial # Differenz von Map-Beginn und Range-Beginn
        right_offset = left_offset + map.length - length  # Differenz von Map-Ende und Range-Ende
        #print("left:", left_offset, " right:", right_offset)
        if left_offset > 0 and left_offset < length and right_offset < 0 and right_offset > -length:  # komplett drin
            mapped_initials.append(map.dest_start)
            mapped_lengths.append(length - left_offset + right_offset)
            unmapped_initials.extend([initial, map.source_start + map.length])
            unmapped_lengths.extend([left_offset, -right_offset])
        elif left_offset > 0 and left_offset < length and right_offset >= 0:  # ragt rechts heraus
            mapped_initials.append(map.dest_start)
            mapped_lengths.append(length - left_offset)
            unmapped_initials.append(initial)
            unmapped_lengths.append(left_offset)
        elif left_offset <= 0 and right_offset < 0 and right_offset > -length:  # ragt links heraus
            mapped_initials.append(map.dest_start - left_offset)
            mapped_lengths.append(-left_offset)
            unmapped_initials.append(initial - left_offset)
            unmapped_lengths.append(length + left_offset)
        elif left_offset <= 0 and right_offset >= 0:  # deckt ab
            mapped_initials.append(map.dest_start - left_offset)
            mapped_lengths.append(length)
        else:  # kein Überlapp
            unmapped_initials.append(initial)
            unmapped_lengths.append(length)
    return Ranges(mapped_initials, mapped_lengths), Ranges(unmapped_initials, unmapped_lengths)

f = open("05/input.txt", "r")
input = f.read()
inputs = input.split("\n\n")
seed_data = [int(x) for x in inputs[0].split(": ")[1].split()]
unmapped_ranges = Ranges(seed_data[::2], seed_data[1::2])
for block in inputs[1:]:
    name, values = block.split(":\n")
    lines = values.split("\n")
    maps = []
    for line in lines:
        dest_range_start, source_range_start, length = line.split()
        maps.append(Map(int(dest_range_start), int(source_range_start), int(length)))
    mapped_ranges_list = []
    for map in maps:
        mapped_ranges = None
        mapped_ranges, unmapped_ranges = map_ranges(unmapped_ranges, map)
        mapped_ranges_list.append(mapped_ranges)
    unmapped_ranges = merge_ranges([*mapped_ranges_list, unmapped_ranges])
    
print(unmapped_ranges.min())
f.close()