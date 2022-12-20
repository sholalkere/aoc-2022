from copy import deepcopy
with open("input.txt", "r") as f:
    lines = f.readlines()

nums = list(map(lambda x: int(x.strip()), lines))
nums = list(zip(nums, (i for i in range(len(nums)))))

numsa = deepcopy(nums)

offset = 0
for i in range(len(numsa)):
    curr = list(filter(lambda x: x[1] == i, numsa))
    curr = curr[0]
    idx_to_remove = numsa.index(curr)
    numsa.pop(idx_to_remove)
    numsa.insert((idx_to_remove + curr[0]) % len(numsa), curr)
    if (idx_to_remove + curr[0]) % len(numsa) == 0:
        offset += 1

numsa = [numsa[(i + offset) % len(numsa)][0] for i in range(len(numsa))]
offset = numsa.index(0)

idxs = [1000, 2000, 3000]
a = sum(numsa[(idx + offset) % len(numsa)] for idx in idxs)
print(a)

numsb = deepcopy(nums)

offset = 0
mult = 811589153
for _ in range(10):
    for i in range(len(numsb)):
        curr = list(filter(lambda x: x[1] == i, numsb))
        curr = curr[0]
        idx_to_remove = numsb.index(curr)
        numsb.pop(idx_to_remove)
        numsb.insert((idx_to_remove + (curr[0] * mult)) % len(numsb), curr)
        if (idx_to_remove + (curr[0] * mult)) % len(numsb) == 0:
            offset += 1

numsb = [numsb[(i + offset) % len(numsb)][0] for i in range(len(numsb))]
offset = numsb.index(0)

b = sum(numsb[(idx + offset) % len(numsb)] for idx in idxs) * mult
print(b)