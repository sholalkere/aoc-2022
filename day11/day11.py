with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip().split() for line in lines]
lines = [[]] + lines

num_monkeys = 8

items = [[int("".join(c for c in item if c.isdigit())) for item in lines[7 * i + 2][2:]] for i in range(num_monkeys)]

inspections = [0 for _ in range(num_monkeys)]
# for round in range(20):
for round in range(10000):
    print(f"round: {round}")
    for monkey in range(num_monkeys):
        for item in items[monkey]:
            inspections[monkey] += 1

            if lines[7 * monkey + 3][-1] == "old":
                other = item
            else:
                other = int(lines[7 * monkey + 3][-1])
            
            if lines[7 * monkey + 3][-2] == "+":
                worry_level = item + other
            elif lines[7 * monkey + 3][-2] == "*":
                worry_level = item * other
            else:
                ValueError("test")

            # worry_level //= 3
            worry_level = worry_level % 9699690 # LCM of worry levels
            if worry_level % int(lines[7 * monkey + 4][-1]) == 0:
                items[int(lines[7 * monkey + 5][-1])].append(worry_level)
            else:
                items[int(lines[7 * monkey + 6][-1])].append(worry_level)
        items[monkey] = []

inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])