import sys

with open("input.txt", "r") as f:
    lines = f.readlines()

a = 0
b = 0

for line in lines:
    ranges = list(map(lambda x: list(map(int, x.split("-"))), line.split(",")))
    if (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]) or (
        ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]
    ):
        a += 1
    if (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][0]) or (
        ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][0]
    ):
        b += 1

print(a)
print(b)
