import json
points = {}
count = 0
point2 = []
tot = 0
def count_score(tree, loc):
    score = 0
    for i in tree:
        if type(tree[i]) == int:
            score += tree[i]
        else:
            score += count_score(tree[i], i)
    global count
    global tot
    if score <= 100000:
        count += score
    point2.append(score)
    return score
def p1(f):
    data = f.read().splitlines()
    data = data[1:]
    tree = {}

    location = ""

    def add(s):
        a =  tree
        if location:
            for i in location.split("."):
                if i:
                    a = a[i]

        if s.startswith("dir"):
            _, name = s.split(" ")
            a[name] = {}
        else:
            size, name = s.split(" ")
            a[name] = int(size)
    i = 0
    while True:
        b = data[i]
        if b.startswith("$"):
            if b[2] == "c":
                _, command, loc = b.split(" ")

                if loc == "/":
                    location = ""
                elif loc == "..":
                    fill = location.split(".")
                    fill.pop()
                    location = ".".join(fill)
                else:
                    location += "." + loc
                i += 1

            else:
                i += 1
                while True:
                    inp = data[i]

                    add(inp)
                    i += 1

                    if i == len(data) or data[i].startswith("$"):
                        break

        if i == len(data):
            break
    tot = count_score(tree, "/")

    return count 






def p2(f):
    data = f.read().splitlines()
    data = data[1:]
    tree = {}

    location = ""

    def add(s):
        a =  tree
        if location:
            for i in location.split("."):
                if i:
                    a = a[i]

        if s.startswith("dir"):
            _, name = s.split(" ")
            a[name] = {}
        else:
            #print(s)
            size, name = s.split(" ")
            a[name] = int(size)
    i = 0
    while True:
        b = data[i]
        if b.startswith("$"):
            if b[2] == "c":
                _, command, loc = b.split(" ")

                if loc == "/":
                    location = ""
                elif loc == "..":
                    fill = location.split(".")
                    fill.pop()
                    location = ".".join(fill)
                else:
                    location += "." + loc
                i += 1

            else:
                i += 1
                while True:
                    inp = data[i]

                    add(inp)
                    i += 1

                    if i == len(data) or data[i].startswith("$"):
                        break

        if i == len(data):
            break
    tot = count_score(tree, "/")

    target =( 30000000 - (70000000 - tot))
    global point2
    point2 = sorted(point2)

    for i in point2:
        if i > target:
            return i