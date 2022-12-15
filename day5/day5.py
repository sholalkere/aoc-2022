import copy
with open("input.txt", "r") as f:
    lines = f.readlines()

a = 0
b = 0

a_stacks = [
    ["H", "R", "B", "D", "Z", "F", "L", "S"],
    ["T", "B", "M", "Z", "R"],
    ["Z", "L", "C", "H", "N", "S"],
    ["S", "C", "F", "J"],
    ["P", "G", "H", "W", "R", "Z", "B"],
    ["V", "J", "Z", "G", "D", "N", "M", "T"],
    ["G", "L", "N", "W", "F", "S", "P", "Q"],
    ["M", "Z", "R"],
    ["M", "C", "L", "G", "V", "R", "T"],
]

b_stacks = copy.deepcopy(a_stacks)


lines = [line.strip() for line in lines]
lines = lines[10:]

for line in lines:
    line = line.split()
    num, fr, to = int(line[1]), int(line[3]), int(line[5])
    fr, to = fr - 1, to - 1

    for _ in range(num):
        to_move = a_stacks[fr][-1]
        a_stacks[fr] = a_stacks[fr][:-1]
        a_stacks[to].append(to_move)

    to_move = b_stacks[fr][-num:]
    b_stacks[fr] = b_stacks[fr][:-num]
    b_stacks[to].extend(to_move)

a = "".join(stack[-1] for stack in a_stacks)
b = "".join(stack[-1] for stack in b_stacks)

print(a)
print(b)