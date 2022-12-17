from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

def process(line):
    line = line.strip()
    return line

lines = list(map(process, lines))
lines = list(lines[0])

rocks = defaultdict(bool)

def new_piece(id, height):
    place_height = height + 4
    if id == 0:
        return set([(2, place_height), (3, place_height), (4, place_height), (5, place_height)])
    elif id == 1:
        return set([(3, place_height + 2), (2, place_height + 1), (3, place_height + 1), (4, place_height + 1), (3, place_height)])
    elif id == 2:
        return set([(4, place_height + 2), (4, place_height + 1), (2, place_height), (3, place_height), (4, place_height)])
    elif id == 3:
        return set([(2, place_height + 3), (2, place_height + 2), (2, place_height + 1), (2, place_height)])
    elif id == 4:
        return set([(2, place_height + 1), (3, place_height + 1), (2, place_height), (3, place_height)])
    raise ValueError("incorrect id")

def valid(piece, floor):
    return all(rock[0] >= 0 and rock[0] < 7 and rock[1] > 0 and rock not in floor for rock in piece)

def try_move(piece, move, floor):
    if move == "<":
        new_piece = set((rock[0] - 1, rock[1]) for rock in piece)
        if valid(new_piece, floor):
            return new_piece, True
    elif move == ">":
        new_piece = set((rock[0] + 1, rock[1]) for rock in piece)
        if valid(new_piece, floor):
            return new_piece, True
    elif move == "v":
        new_piece = set((rock[0], rock[1] - 1) for rock in piece)
        if valid(new_piece, floor):
            return new_piece, True
    else:
        raise ValueError("invalid move")

    return piece, False

def print_game(piece, rocks, height):
    s = ""
    for y in range(height, -1, -1):
        for x in range(0, 7):
            if rocks[(x, y)] or (x, y) in piece:
                s += "#"
            else:
                s += "."
        s += "\n"

    print(s)

floor = set([(x, 0) for x in range(7)])

# copied from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/17.py
def signature(floor):
    maxy = max(y for (x, y) in floor)
    return frozenset([(x, maxy - y) for (x, y) in floor if maxy - y <= 30])    

seen = {}
height = 0
move_i = 0
tot = 1000000000000
added = 0
i = 0

while i < tot:
    piece = new_piece(i % 5, height)
    while True:
        piece, ok = try_move(piece, lines[move_i % len(lines)], floor)
        move_i = (move_i + 1) % len(lines)
        piece, ok = try_move(piece, "v", floor)
        if not ok:
            break

    floor |= piece
    height = max(y for (x, y) in floor)

    # copied from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/17.py
    save = (move_i, i % 5, signature(floor))
    if save in seen and i >= 2022: 
        (old_iter, old_height) = seen[save]
        dheight = height - old_height
        diter = i - old_iter
        amt = (tot - height) // diter
        added += amt * dheight
        i += amt * diter

    seen[save] = (i, height)

    i += 1
    if i == 2022:
        print(height)

print(height + added)