with open("input.txt") as f:
    data = f.read().splitlines()
points = 0
for row in data:
    a, b = row.split()
    if a == "A":
        if b == "Y":
            points += 1 + 3
        if b == "X":
            points += 3
        if b == "Z":
            points += 6 + 2
    elif a == "B":
        if b == "Y":
            points += 2 + 3
        if b == "X":
            points += 1
        if b == "Z":
            points += 3 + 6
    elif a == "C":
        if b == "X":
            points += 2
        if b == "Z":
            points += 6 + 1
        if b == "Y":
            points += 3 + 3
print(points)
