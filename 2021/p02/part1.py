with open("input.txt") as f:
    data = f.read().splitlines()

pos, depth = 0, 0

for command in data:
    c, n = command.split()

    if c == "forward":
        pos += int(n)
    elif c == "down":
        depth += int(n)
    else:
        depth -= int(n)

print(pos*depth)
