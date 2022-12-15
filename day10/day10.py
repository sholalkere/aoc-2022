with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip().split() for line in lines]

flattened = [el for line in lines for el in line]

def signal_strentgh(time, flattened):
    result = 1
    for instruction in flattened[:time - 1]:
        if instruction not in ["addx", "noop"]:
            result += int(instruction)

    return result * time

a = sum(signal_strentgh(time, flattened) for time in [20, 60, 100, 140, 180, 220])
print(a)

crt = [["." for _ in range(40)] for _ in range(6)]

def print_crt():
    print("\n".join("".join(line) for line in crt))

def register_value(time, flattened):
    result = 1
    for instruction in flattened[:time - 1]:
        if instruction not in ["addx", "noop"]:
            result += int(instruction)

    return result

for row in range(6):
    for col in range(1, 41):
        time = row * 40 + col
        sprite_location = register_value(row * 40 + col, flattened)
        if abs(col - 1 - sprite_location) <= 1:
            crt[row][col - 1] = "#"

print_crt()