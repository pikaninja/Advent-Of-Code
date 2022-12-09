def p1(f):
    data = f.read().splitlines()
    vis = set([(0,0)])
    h = [0, 0]
    t = [0, 0]


    def update_tail():


        movex = [1, -1, 0, 0, 1, -1, -1, 1, 0]
        movey = [0, 0, 1, -1, 1, -1, 1, -1, 0]


        for i in range(9):
            if t[0] + movex[i] == h[0] and t[1] + movey[i] == h[1]:

                return

        if h[0] == t[0]:
            if t[1] < h[1]:
                t[1] += 1
            else:
                t[1] -= 1
        elif h[1] == t[1]:
            if t[0] < h[0]:
                t[0] += 1
            else:
                t[0] -= 1
        else:
            if t[1] < h[1]:
                t[1] += 1
            else:
                t[1] -= 1

            if t[0] < h[0]:
                t[0] += 1
            else:
                t[0] -= 1


        vis.add((t[0], t[1]))
        

    for i in data:
        s, c = i.split()
        c = int(c)



        if s == "R":
            for i in range(c):
                h[1] += 1
                update_tail()
        elif s == "L":
            for i in range(c):
                h[1] -= 1
                update_tail()
        elif s == "U":
            for i in range(c):
                h[0] += 1
                update_tail()
        else:
            for i in range(c):
                h[0] -= 1
                update_tail()


    return len(vis)





def p2(f):
    data = f.read().splitlines()
    vis = set([(0,0)])
    tails = [[0, 0] for i in range(10)]
    def update_tail():

        for i in range(1, 10):
            t = tails[i]
            h = tails[i-1]
            movex = [1, -1, 0, 0, 1, -1, -1, 1, 0]
            movey = [0, 0, 1, -1, 1, -1, 1, -1, 0]
    
            done = False
            for i in range(9):
                if t[0] + movex[i] == h[0] and t[1] + movey[i] == h[1]:
                    done = True
                    continue
            if done:
                continue
                    
    
            if h[0] == t[0]:
                if t[1] < h[1]:
                    t[1] += 1
                else:
                    t[1] -= 1
            elif h[1] == t[1]:
                if t[0] < h[0]:
                    t[0] += 1
                else:
                    t[0] -= 1
            else:
                if t[1] < h[1]:
                    t[1] += 1
                else:
                    t[1] -= 1
    
                if t[0] < h[0]:
                    t[0] += 1
                else:
                    t[0] -= 1
        if i == 8:
            vis.add((t[0], t[1]))
        

    for i in data:
        s, c = i.split()
        c = int(c)



        if s == "R":
            for i in range(c):
                tails[0][1] += 1
                update_tail()
        elif s == "L":
            for i in range(c):
                tails[0][1] -= 1
                update_tail()
        elif s == "U":
            for i in range(c):
                tails[0][0] += 1
                update_tail()
        else:
            for i in range(c):
                tails[0][0] -= 1
                update_tail()



    return len(vis)
