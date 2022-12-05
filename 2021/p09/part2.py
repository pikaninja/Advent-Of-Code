with open("input.txt") as f:
    data = f.read().splitlines()

n = len(data)
m = len(data[0])

risk = 0
change_x = [1, -1, 0, 0]
change_y = [0, 0, 1, -1]

vis = [[False for i in range(m)] for j in range(n)]

def check(pos_x: int, pos_y: int, old: int):
    if pos_x < 0 or pos_x >= n or pos_y < 0 or pos_y >= m or vis[pos_x][pos_y] or data[pos_x][pos_y] == "9" or int(data[pos_x][pos_y]) < old:
        return 0

    vis[pos_x][pos_y] = True
    count = 1
    old = int(data[pos_x][pos_y])
    count += check(pos_x + 1, pos_y, old)
    count += check(pos_x - 1, pos_y, old)
    count += check(pos_x, pos_y - 1, old)
    count += check(pos_x, pos_y + 1, old)

    return count



counts = []



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
            counts.append(check(x, y, -1))
            

counts = sorted(counts)

print(counts[-1] * counts[-2] * counts[-3])




