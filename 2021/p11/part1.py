with open("input.txt") as f:
    data = f.read().splitlines() 

data = [list(map(int, i)) for i in data]

n = len(data)
m = len(data[0])

def inc():
    for x in range(n):
        for y in range(m):
            data[x][y] += 1

flashed = []

def real_flash(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or flashed[x][y]:
        return 0

    flashed[x][y] = True

    movement = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    count = 1

    for move in movement:
        new_x = x + move[0]
        new_y = y + move[1]

        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
            continue
    
        data[new_x][new_y] += 1
        if data[new_x][new_y] > 9:
            count += real_flash(new_x, new_y)
    return count


def flash():
    global flashed
    flashed = [[False for i in range(m)] for j in range(n)]
    count = 0
    for x in range(n):
        for y in range(m):
            if data[x][y] > 9:
                count += real_flash(x, y)
    return count

def reset():
    for i in range(n):
        for j in range(m):
            if flashed[i][j]:
                data[i][j] = 0
            

count = 0
for i in range(100):
    inc()
    count += flash()
    reset()

    for i in data:
        for j in i:
            print(j, end = " ")
        print()

    print()

print(count)


