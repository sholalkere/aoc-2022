with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.split() for line in lines]

head = (0, 0)
tail = (0, 0)

visited = set()
visited.add(tail)

ok = set([(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]])

def diff(u, v):
    return (u[0] - v[0], u[1] - v[1])

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def new_tail(head, tail):
    if diff(head, tail) in ok:
        return tail

    to_move = None
    min_dis = float('inf')

    for move in ok:
        new_dis = sum(map(lambda x: x ** 2, diff(add(tail, move), head)))
        if  new_dis < min_dis:
            to_move = move
            min_dis = new_dis
    
    return add(tail, to_move)

dir = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

for line in lines:
    d, n = line
    for _ in range(int(n)):
        head = add(head, dir[d])
        tail = new_tail(head, tail)
        visited.add(tail)

a = len(visited)
print(a)

rope = [(0, 0) for _ in range(10)]

visited = set()
visited.add(rope[-1])

for line in lines:
    d, n = line
    for _ in range(int(n)):
        rope[0] = add(rope[0], dir[d])
        for i in range(1, 10):
            rope[i] = new_tail(rope[i - 1], rope[i])
        visited.add(rope[-1])

b = len(visited)
print(b)