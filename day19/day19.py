with open("input.txt", "r") as f:
    lines = f.readlines()

# with open("debug.txt", "r") as f:
#     lines = f.readlines()

lines = [list(map(lambda x: " " if not x.isnumeric() else x, list(line))) for line in lines]
lines = ["".join(line).split() for line in lines]
lines = [list(map(int, line)) for line in lines]


print(lines)