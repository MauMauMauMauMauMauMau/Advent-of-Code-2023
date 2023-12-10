input = open("01/input.txt", "r")
lines = input.readlines()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
for line in lines:
    # print(line)
    first = ""
    first_digit_pos = 0
    for pos, char in enumerate(line):
        if char in digits:
            first = char
            first_digit_pos = pos
            break

    last = ""
    last_digit_pos = 0
    for pos, char in enumerate(reversed(line)):
        if char in digits:
            last = char
            last_digit_pos = len(line) - pos - 1
            break
    
    # print("first digit:", first, "last digit:", last)

    number_poss_f = [line.find(number) for number in numbers]
    for pos, entry in enumerate(number_poss_f):
        if entry == -1:
            number_poss_f[pos] = "nil"
    number_poss_only_digit_f = [i for i in number_poss_f if isinstance(i, int)]

    # print("forward number pos:", number_poss_f, number_poss_only_digit_f)

    if any(number_pos < first_digit_pos for number_pos in number_poss_only_digit_f):
        first = str(number_poss_f.index(min(number_poss_only_digit_f)) + 1)
        # print("earlier string found", first)
    
    number_poss_b = [len(line) - line[::-1].find(number[::-1]) - 1 for number in numbers]
    for pos, entry in enumerate(number_poss_b):
        if entry == len(line):
            number_poss_b[pos] = "nil"
    number_poss_only_digit_b = [i for i in number_poss_b if isinstance(i, int)]

    # print("backward number pos:", number_poss_b, number_poss_only_digit_b)

    if any(number_pos > last_digit_pos for number_pos in number_poss_only_digit_b):
        last = str(number_poss_b.index(max(number_poss_only_digit_b)) + 1)
        # print("later string found", last)
    
    # print(first + last)
    sum += int(first + last)

print(sum)    

input.close()