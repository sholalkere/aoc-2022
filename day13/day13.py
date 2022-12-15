import ast
from functools import cmp_to_key

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line != "\n"]

def parse(s):
    return ast.literal_eval(s)

lines = [parse(line) for line in lines]

def valid(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            fst = a[i]
            snd = b[i]
            if valid(fst, snd) == -1:
                return -1
            elif valid(fst, snd) == 0:
                continue
            else:
                return 1
            
        if len(a) < len(b):
            return -1
        elif len(a) == len(b):
            return 0
        else:
            return 1
    
    if isinstance(a, int) and isinstance(b, list):
        return valid([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return valid(a, [b])

def valid_cmp(a, b):
    return valid(a, b) # - 1

a = 0
for i in range(0, len(lines), 2):
    if valid(lines[i], lines[i + 1]) == -1:
        a += (i // 2) + 1
print(a)

sorted_lines = sorted(lines + [[[2]]] + [[[6]]] , key=cmp_to_key(valid_cmp))
idx1 = sorted_lines.index([[2]]) + 1
idx2 = sorted_lines.index([[6]]) + 1
print(idx1 * idx2)
