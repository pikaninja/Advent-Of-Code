with open("input.txt") as f:
    data = f.read().split("\n\n")

maxi = 0
counts = []

for i in data:
    sumi = 0
    for j in i.split("\n"):
        if j:
            sumi += int(j)
    counts.append(sumi)


counts.sort()

print(counts[-1] + counts[-2] + counts[-3])


