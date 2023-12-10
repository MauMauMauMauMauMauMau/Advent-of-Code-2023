input = open("01/input.txt", "r")
lines = input.readlines()

sum = 0

for line in lines:
    first, last = "", ""
    for char in line:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            first = char
            break

    for char in reversed(line):
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            last = char
            break
    
    print(first, last)
    sum += int(first + last)

print(sum)    

input.close()