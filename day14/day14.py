from collections import defaultdict
from copy import deepcopy

with open("input.txt", "r") as f:
    lines = f.readlines()

def process(line):
    line = line.strip()
    line = line.split()
    line = list(filter(lambda x: x != "->", line))
    line = list(map(lambda pair: (int(pair.split(",")[0]), int(pair.split(",")[1])), line))
    return line

lines = list(map(process, lines))

rocks = defaultdict(bool)

for line in lines:
    prev = line[0]
    for curr in line[1:]:
        if prev[0] == curr[0]:
            for y in range(min(prev[1], curr[1]), max(prev[1], curr[1]) + 1):
                rocks[curr[0], y] = True
        else:
            for x in range(min(prev[0], curr[0]), max(prev[0], curr[0]) + 1):
                rocks[x, curr[1]] = True
        prev = curr

def get_minx(d):
    return min(key[0] for key, val in d.items())

def get_maxx(d):
    return max(key[0] for key, val in d.items())

def get_miny(d):
    return min(key[1] for key, val in d.items())

def get_maxy(d):
    return max(key[1] for key, val in d.items())

maxy = get_maxy(rocks)
threshold = 200
for x in range(get_minx(rocks) - threshold, get_maxx(rocks) + threshold + 1):
    rocks[(x, maxy + 2)] = True

obstructions = deepcopy(rocks)

def print_state():
    minx, maxx, miny, maxy = get_minx(obstructions), get_maxx(obstructions), get_miny(obstructions), get_maxy(obstructions)
    s = ""

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if rocks[(x, y)]:
                s += "#"
            elif obstructions[(x, y)]:
                s += "+"
            else:
                s += "."
        s += "\n"

    print(s)

def add_sand():
    maxy = get_maxy(rocks)
    x, y = 500, -1

    while True:
        if y > maxy:
            return False
        if not obstructions[(x, y + 1)]:
            x, y = x, y + 1
        elif not obstructions[(x - 1, y + 1)]:
            x, y = x - 1, y + 1
        elif not obstructions[(x + 1, y + 1)]:
            x, y = x + 1, y + 1
        else:
            break

    obstructions[(x, y)] = True

    return (x, y) != (500, 0)

added = 0
while add_sand():
    added += 1

print(added + 1)
