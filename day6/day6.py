with open("input.txt", "r") as f:
    lines = f.readlines()

line = lines[0]

for i in range(4, len(line)):
    if len(set(line[i - 4 : i])) == 4:
        print(i)
        break

for i in range(14, len(line)):
    if len(set(line[i - 14 : i])) == 14:
        print(i)
        break
