from collections import deque

with open("input.txt", "r") as f:
    lines = f.readlines()
    
lines = [line.strip() for line in lines]
lines = [line.split(",") for line in lines]
lines = [list(map(int, line)) for line in lines]

seen = set()
a = 0
for line in lines:
    x, y, z = line
    if (x + 1, y, z) in seen:
        a -= 2
    if (x, y + 1, z) in seen:
        a -= 2
    if (x, y, z + 1) in seen:
        a -= 2
    if (x - 1, y, z) in seen:
        a -= 2
    if (x, y - 1, z) in seen:
        a -= 2
    if (x, y, z - 1) in seen:
        a -= 2
    a += 6
    seen.add((x, y, z))

print(a)

outside = set()
inside = set()

# copied from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/18.py
def can_reach(x,y,z):
    if (x,y,z) in outside:
        return True
    if (x,y,z) in inside:
        return False
    
    visited = set()
    q = deque([(x,y,z)])

    while q:
        x, y, z = q.popleft()

        if (x, y, z) in seen or (x, y, z) in visited:
            continue

        visited.add((x,y,z))

        if len(visited) > 5000:
            for p in visited:
                outside.add(p)
            return True
        
        q.append((x+1,y,z))
        q.append((x-1,y,z))
        q.append((x,y+1,z))
        q.append((x,y-1,z))
        q.append((x,y,z+1))
        q.append((x,y,z-1))

    for p in visited:
        inside.add(p)

    return False

b = 0
for line in lines:
    x, y, z = line
    if can_reach(x + 1, y, z):
        b += 1
    if can_reach(x, y + 1, z):
        b += 1
    if can_reach(x, y, z + 1):
        b += 1
    if can_reach(x - 1, y, z):
        b += 1
    if can_reach(x, y - 1, z):
        b += 1
    if can_reach(x, y, z - 1):
        b += 1
print(b)