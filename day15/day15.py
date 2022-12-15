with open("input.txt", "r") as f:
    lines = f.readlines()

def process(line):
    line = line.strip()
    line = line.split()
    line[2] = line[2][2:-1]
    line[3] = line[3][2:-1]

    line[-2] = line[-2][2:-1]
    line[-1] = line[-1][2:]
    line = [int(line[i]) for i in [2, 3, -2, -1]]
    return line

lines = list(map(process, lines))

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

y = 10
y = 2000000

def cant_contain(y):
    cant_contain = []

    for line in lines:
        x1, y1, x2, y2 = line
        p1 = (x1, y1)
        p2 = (x2, y2)

        d = dist(p1, p2)
        tol = d - abs(y1 - y)
        if tol >= 0:
            cant_contain += [[x1 - tol, x1 + tol]]

    return cant_contain

cant = cant_contain(y)

def merge(l):
    l.sort()
    res = []
    res.append(l[0])

    for i in l[1:]:
        if res[-1][0] <= i[0] <= res[-1][-1]:
            res[-1][-1] = max(res[-1][-1], i[-1])
        else:
            res.append(i)

    return res

merged = merge(cant)

a = merged[0][1] - merged[0][0] + 1

seen = set()
for line in lines:
    x1, y1, x2, y2 = line
    if y1 ==  y and (x1, y1) not in seen:
        a -= 1
        seen.add((x1, y1))
    if y2 == y and (x2, y2) not in seen:
        a -= 1
        seen.add((x2, y2))

print(a)

for y in range(4000000, -1, -1):
    cnt = merge(cant_contain(y))
    if len(cnt) != 1:
        b = ((cnt[0][1] + 1) * 4000000) + y
        break

print(b)