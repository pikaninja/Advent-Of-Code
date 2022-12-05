with open("input.txt") as f:
    data = f.read().splitlines()

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
mp = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

def parse(code: str):
    stack = []
    for i in code:
        print(stack)
        if i in "([<{":
            stack.append(i)
        else:
            print(stack[-1])
            if mp[stack[-1]] == i:
                stack.pop()
            else:
                print(i)
                return points[i]
    return 0

p = 0
for row in data:
    p += parse(row)

print(p)
                
                
