import sys
from collections import defaultdict, deque

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [list(line) for line in lines]

start = None
end = None
starts = []

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
            lines[i][j] = "a"
            starts += [(i, j)]
        elif char == "a":
            starts += [(i, j)]
        elif char == "E":
            end = (i, j)
            lines[i][j] = "z"


def height_diff(p, q):
    return ord(lines[q[0]][q[1]]) - ord(lines[p[0]][p[1]])

def neighbors(v):
    res = []
    for diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new = (v[0] + diff[0], v[1] + diff[1])
        if new[0] >= 0 and new[0] < len(lines) and new[1] >= 0 and new[1] < len(lines[0]) and height_diff(v, new) <= 1:
            res += [new]

    return res

def dist(start, end):
    visited = set()
    dists = defaultdict(lambda: float("inf"))
    parent = {}
    queue = deque([start])
    dists[start] = 0
    visited.add(start)

    while queue:
        v = queue.popleft()
        if v == end:
            return dists[end]
        for neighbor in neighbors(v):
            if neighbor not in visited:
                parent[neighbor] = v
                visited.add(neighbor)
                dists[neighbor] = dists[v] + 1
                queue.append(neighbor)


print(dist(start, end))
print(min(filter(lambda x: x is not None, [dist(start, end) for start in starts] )))
