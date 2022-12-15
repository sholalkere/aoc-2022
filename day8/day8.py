with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
width = len(lines[0])
height = len(lines)
lines = [list(line) for line in lines]
lines = list(map(lambda x: list(map(int, x)), lines))

visible = set()
a = 0

def valid(l):
    if len(l) <= 1:
        return True
    else:
        return l[-1] > max(l[:-1])

for i in range(height):
    for j in range(width):
        if valid(lines[i][:j + 1]):
            visible.add((i, j))
        elif valid((lines[i][j:])[::-1]):
            visible.add((i, j))
        elif valid([line[j] for line in lines[:i + 1]]):
            visible.add((i, j))
        elif valid([line[j] for line in lines[i:]][::-1]):
            visible.add((i, j))


a = len(visible)
print(a)

def scenic_score(row, col):
    left = 0
    new_col = col - 1
    while new_col >= 0 and lines[row][new_col] <= lines[row][col]:
        left += 1
        if lines[row][new_col] == lines[row][col]:
            break
        new_col -= 1

    right = 0
    new_col = col + 1
    while new_col < width and lines[row][new_col] <= lines[row][col]:
        right += 1
        if lines[row][new_col] == lines[row][col]:
            break
        new_col += 1

    up = 0
    new_row = row - 1
    while new_row >= 0 and lines[new_row][col] <= lines[row][col]:
        up += 1
        if lines[new_row][col] == lines[row][col]:
            break
        new_row -= 1

    down = 0
    new_row = row + 1
    while new_row < height and lines[new_row][col] <= lines[row][col]:
        down += 1
        if lines[new_row][col] == lines[row][col]:
            break
        new_row += 1
    return left * right * up * down

b = -float('inf')
for i in range(height):
    for j in range(width):
        b = max(b, scenic_score(i, j))

print(b)