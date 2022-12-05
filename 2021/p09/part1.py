with open("input.txt") as f:
    data = f.read().splitlines()

risk = 0
change_x = [1, -1, 0, 0]
change_y = [0, 0, 1, -1]

for x, row in enumerate(data):
    for y, item in enumerate(row):
        work = True
        for i in range(4):
            new_x = x + change_x[i]
            new_y = y + change_y[i]
            if new_x < 0 or new_x >= len(data) or new_y < 0 or new_y >= len(row):
                continue

            if int(data[new_x][new_y]) <= int(item):
                work = False
                break
        if work:
            risk += int(item) + 1

print(risk)
        



