with open("input.txt") as f:
    data = f.read().splitlines()

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
mp = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}
mp2 = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}

def parse(code: str):
    stack = []
    for i in code:
        if i in "([<{":
            stack.append(i)
        else:
            if mp[stack[-1]] == i:
                stack.pop()
            else:
                return 0
    pt = 0
    for i in stack[::-1]:
        pt *= 5
        pt += points[mp[i]]
        print(mp[i], end = " ")
    print(pt)

    return pt

p = []
for row in data:
    if a := parse(row):
     p.append(a)

print(p)
p.sort()
print(p[len(p)//2])
                
                
