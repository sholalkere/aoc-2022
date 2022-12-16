from collections import defaultdict
from functools import cache
from copy import deepcopy

with open("input.txt", "r") as f:
    lines = f.readlines()

def process(line):
    line = line.strip()
    line = line.replace(",","")
    line = line.split()
    line = [line[1], line[4], line[9:]]
    line[1] = int(line[1][5:-1])
    line[2] = list(map(str.strip, line[2]))
    return line

lines = list(map(process, lines))

neighbors = {}
flow_rate = {}
for line in lines:
    neighbors[line[0]] = set(line[2])
    flow_rate[line[0]] = line[1]

dists = defaultdict(lambda: float('inf'))

for k, v in neighbors.items():
    dists[(k, k)] = 0
    for t in v:
        dists[(k, t)] = 1
        dists[(t, k)] = 1

for k in neighbors.keys():
    for i in neighbors.keys():
        for j in neighbors.keys():
            dists[(i, j)] = min(dists[(i, j)], dists[(i, k)] + dists[(k, j)])

@cache
def dfs(curr, time, remaining):
    remaining = list(remaining)
    res = 0
    for nxt in remaining:
        if dists[(curr, nxt)] < time:
            new_remaining = deepcopy(remaining)
            new_remaining.pop(new_remaining.index(nxt))
            new_remaining = tuple(new_remaining)
            res = max(res, flow_rate[nxt] * (time - dists[(curr, nxt)] - 1) + dfs(nxt, time - dists[(curr, nxt)] - 1, new_remaining))

    return res

to_consider = tuple(valve for valve in flow_rate if flow_rate[valve] > 0)

a = dfs("AA", 30, to_consider)
print(a)

def dfs2(curr, time, remaining):
    res = dfs("AA", 26, remaining)
    remaining = list(remaining)
    for nxt in remaining:
        if dists[(curr, nxt)] < time:
            new_remaining = deepcopy(remaining)
            new_remaining.pop(new_remaining.index(nxt))
            new_remaining = tuple(new_remaining)
            res = max(res, flow_rate[nxt] * (time - dists[(curr, nxt)] - 1) + dfs2(nxt, time - dists[(curr, nxt)] - 1, new_remaining))

    return res

b = dfs2("AA", 26, to_consider)
print(b)
