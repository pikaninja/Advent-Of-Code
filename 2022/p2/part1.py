with open("input.txt") as f:
    data = f.read().splitlines()
points = 0
for row in data:
    a, b = row.split()
    if a == "A":
        if b == "Y":
            points += 2 + 6
        if b == "X":
            points += 1 + 3
        if b == "Z":
            points += 3 
    elif a == "B":
        if b == "Y":
            points += 2 + 3
        if b == "X":
            points += 1
        if b == "Z":
            points += 3 + 6
    elif a == "C":
        if b == "Y":
            points += 2
        if b == "X":
            points += 6 + 1
        if b == "Z":
            points += 3 + 3
print(points)
