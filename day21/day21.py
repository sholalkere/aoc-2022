from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.replace(":", "=") for line in lines]

for _ in range(int(len(lines) ** 0.5)):
    for line in lines:
        try:
            exec(line)
        except:
            pass

print(int(root))

