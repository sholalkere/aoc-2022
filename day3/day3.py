import sys
from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()

def priority(c):
    return (ord(c) - ord("a") + 1 + 58) % 58


def split(s):
    return s[: len(s) // 2], s[len(s) // 2 :]


def intersection(s):
    s1 = s[0]
    s2 = s[1]
    c = set(s1) & set(s2)
    for key in c:
        return key


def intersection3(s):
    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    c = set(s1) & set(s2) & set(s3)
    for key in c:
        return key


a = sum(priority(intersection(split(line))) for line in lines)
print(a)

b = sum(priority(intersection3((lines[i], lines[i + 1], lines[i + 2]))) for i in range(0, len(lines), 3))
print(b)
