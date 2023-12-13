# parse data
f = open("12/test.txt", "r")
lines = f.readlines()
assortments = []
labels = []
for line in lines:
    assortment, label = line.strip().split()
    assortment = "?".join([assortment for i in range(5)])
    label = [int(i) for i in label.split(',')] * 5
    assortments.append(assortment)
    labels.append(label)
f.close()

# solution without brute force
