import sys
with open("input.txt") as f:
    data = f.read().split("\n\n")


def parse(data):
    nums = list(map(int, data[0].split(",")))
    data = data[1:]

    bingo = []
    for bing in data:
        bing = bing.splitlines()

        b = []
        for row in bing:
            row = row.strip()
            b.append(list(map(lambda m: [int(m), False], row.split())))
        bingo.append(b)

    return nums, bingo

def check_win(board):
    for i in range(5):
        if board[i][0][1] and board[i][1][1] and board[i][2][1] and board[i][3][1] and board[i][4][1]:
            return True
        if board[0][i][1] and board[1][i][1] and board[2][i][1] and board[3][i][1] and board[4][i][1]:
            print("hi")
            return True

    return False




nums, boards = parse(data)


for num in nums:
    next_board = []
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j][0] == num:
                    board[i][j][1] = True
        if check_win(board):
            ans = 0
            for row in board:
                for item in row:
                    if not item[1]:
                        ans += item[0]
            print(ans, num)
        else:
            next_board.append(board)
    boards = next_board

