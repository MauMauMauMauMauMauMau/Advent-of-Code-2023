# parse data
f = open("12/input.txt", "r")
lines = f.readlines()
assortments = []
labels = []
for line in lines:
    assortment, label = line.strip().split()
    label = [int(i) for i in label.split(',')]
    assortments.append(assortment)
    labels.append(label)
f.close()


def check_assortment(assortment, label):
    index = 0
    counters = []
    while index < len(assortment):
        counter = 0
        if assortment[index] == '#':
            while assortment[index] == '#':
                counter += 1
                index += 1
                if index >= len(assortment): break
        if counter > 0: counters.append(counter)
        index += 1
    if counters == label: return True
    else: return False


def all_possible_assortments(initial_assortment):
    # find all question marks
    question_marks = []
    index = 0
    while index < len(initial_assortment):
        index = initial_assortment.find('?', index)
        if index == -1: break
        question_marks.append(index)
        index += 1
    
    # iterate through all possibilities
    possible_assortments = []
    for i in range (0, 2 ** len(question_marks)):
        assortment = initial_assortment
        for q, q_loc in enumerate(question_marks):
            if i % 2 ** (q + 1) >= 2 ** q:
                assortment = assortment[:q_loc] + '#' + assortment[q_loc + 1:]
            else:
                assortment = assortment[:q_loc] + '.' + assortment[q_loc + 1:]
        possible_assortments.append(assortment)
    return possible_assortments


sum = 0
for i, (initial_assortment, label) in enumerate(zip(assortments, labels)):
    # print("Checking", initial_assortment, "with label", label)
    number_of_arrangements = 0
    for possible_assortment in all_possible_assortments(initial_assortment):
        if check_assortment(possible_assortment, label): number_of_arrangements += 1
    # print("  Found", number_of_arrangements, "possible arrangements")
    sum += number_of_arrangements
    print(f"{(i + 1)/len(assortments):.2%} done")
print("-" * 50 + "\nsum =", sum)