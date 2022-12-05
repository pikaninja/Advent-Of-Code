with open("input.txt") as f:
    data = f.read().splitlines()

board = [[0 for i in range(1000)] for j in range(1000)]



for line in data:
    print(line)
    p1, p2 = line.split(" -> ")
    p1 = list(map(int, p1.split(",")))
    p2 = list(map(int, p2.split(",")))

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if x1 == x2:

        for i in range(min([y1, y2]), max([y1, y2])+1):
            board[x1][i] += 1
    elif y1 == y2:
        for i in range(min([x1, x2]), max([x1, x2])+1):

            board[i][y1] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        y = 0
        diffy = y2 - y1

        if diffy > 0:
            diffy = 1
        else:
            diffy = -1

        for i in range(x2-x1 + 1):
            board[x1 + i][y1 + y] += 1
            y += diffy




ans = 0
for i, row in enumerate(board):
    for j, item in enumerate(row):
        if item >= 2:
            ans += 1

print(ans)

