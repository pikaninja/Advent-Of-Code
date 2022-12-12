def p1(f):
    data = f.read().splitlines()
    mp = []
    q = []
    end = []
    n = len(data)
    m = len(data[0])
    for x, i in enumerate(data):
        a = []
        for y, j in enumerate(i):
            if j == "S" or j == "a":
                a.append(0)
                q.append([x, y, 9])
            elif j == "E":
                a.append(ord("z") - ord("a"))
                end = [x, y]
            else:
                a.append(ord(j) - ord("a"))
        mp.append(a)
      
    vis = [[False for i in range(m)] for j in range(n)]
   
    vis_2 = []

   
    while len(q) != 0:
        top = q[0]
        if vis[top[0]][top[1]]:
            q.pop(0)
            continue
   
        vis[top[0]][top[1]] = True
        vis_2.append((top[0], top[1]))
        q.pop(0)
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
   
        for dir in move:
            x, y, c = top
            new_x = x + dir[0]
            new_y = y + dir[1]
            def valid():
                return new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and mp[x][y] + 1 >= mp[new_x][new_y] and not vis[new_x][new_y] and not (new_x, new_y) in vis_2
            if valid():
                if [new_x, new_y] == end:
                    return c+1
                q.append([new_x, new_y, c + 1])

def p2(f):
    data = f.read().splitlines()
    mp = []
    q = []
    end = []
    n = len(data)
    m = len(data[0])
    possible = []
    for x, i in enumerate(data):
        a = []
        for y, j in enumerate(i):
            if j == "S" or j == "a":
                a.append(0)
                possible.append([x, y, 0])
            elif j == "E":
                a.append(ord("z") - ord("a"))
                end = [x, y]
            else:
                a.append(ord(j) - ord("a"))
        mp.append(a)

    mini = 9999999
    for idx, start in enumerate(possible):
        print(idx, "/",len(possible))
        q = []
        vis = [[False for i in range(m)] for j in range(n)]
        vis_2 = []
        q.append(start)

        while len(q) != 0:
            top = q[0]
            if vis[top[0]][top[1]]:
                q.pop(0)
                continue
            vis[top[0]][top[1]] = True
            vis_2.append((top[0], top[1]))
            q.pop(0)
            done = False

            move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir in move:
                x, y, c = top

                new_x = x + dir[0]
                new_y = y + dir[1]

                def valid():
                    return new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and mp[x][y] + 1 >= mp[new_x][new_y] and not vis[new_x][new_y] and not (new_x, new_y) in vis_2
                if valid():
                    if [new_x, new_y] == end:
                        mini = min(c+1, mini)
                        done = True
                        break
                    q.append([new_x, new_y, c + 1])
            if done:
                break

    return mini
