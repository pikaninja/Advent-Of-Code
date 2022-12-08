
def visible(trees, x, y):

    worked = 0
    for i in range(0, x):
        if trees[i][y] >= trees[x][y]:
            worked += 1
            break
            print('1')


    for i in range(x+1, len(trees)):
        if trees[i][y] >= trees[x][y]:
            worked += 1
            break
            print('2')

    for j in range(0, y):
        if trees[x][j] >= trees[x][y]:
            worked += 1
            break
            print('3')

    for j in range(y+1, len(trees[0])):
        if trees[x][j] >= trees[x][y]:
            worked += 1
            break
            print('4')
    return worked < 4

def p1(f):
    data = f.read().splitlines()
    trees = []

    for i in data:
        a = []
        for j in i:
            a.append(int(j))
        trees.append(a)

    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if visible(trees, x, y):
                count += 1

    return count


    

def count_distance(trees, x, y):
    count = 0
    ans = 1
    for i in range(x-1, -1, -1):
        if trees[i][y] < trees[x][y]:
            count += 1
        else:
            count += 1
            break
    ans *= count
    count = 0
    for i in range(y-1, -1, -1):
        if trees[x][i] < trees[x][y]:
            count += 1
        else:
            count += 1
            break
    ans *= count
    count = 0
    for i in range(x+1, len(trees)):
        if trees[i][y] < trees[x][y]:
            count += 1
        else:
            count += 1
            break
    ans *= count
    count = 0
    for i in range(y+1, len(trees[0])):
        if trees[x][i] < trees[x][y]:
            count += 1
        else:
            count += 1
            break
    ans *= count
    return ans

def p2(f):
    data = f.read().splitlines()
    trees = []

    for i in data:
        a = []
        for j in i:
            a.append(int(j))
        trees.append(a)

    count = 0
    print(count_distance(trees, 1, 2))
    maxi = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            view = count_distance(trees, x, y)
            if view > maxi:
                maxi = view
    

    return maxi