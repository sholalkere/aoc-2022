from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()


lines = map(lambda x: x.strip().split(" "), lines)
lines = list(lines)

directories = defaultdict(int)
cwd = [""]

idx = 0
while idx < len(lines):
    line = lines[idx]
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                cwd = [""]
            elif line[2] == "..":
                cwd.pop()
            else:
                cwd += [line[2]]
            idx += 1
        elif line[1] == "ls":
            new_idx = idx + 1
            while new_idx < len(lines) and lines[new_idx][0] != "$":
                curr_line = lines[new_idx]
                if curr_line[0] != "dir":
                    for i in range(1, len(cwd) + 1):
                        directories["/".join(cwd[:i])] += int(curr_line[0])
                new_idx += 1
            idx = new_idx


a = 0
for k, v in directories.items():
    if v <= 100000:
        a += v

print(a)

total = directories[""]
threshold = total - 40000000

b = float("inf")
for k, v in directories.items():
    if v >= threshold:
        b = min(b, v)

print(b)
