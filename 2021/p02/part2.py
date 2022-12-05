with open("input.txt") as f:
    data = f.read().splitlines()

pos, depth, aim = 0, 0, 0

for command in data:
    c, n = command.split()

    if c == "forward":
        pos += int(n)
        depth += int(n) * aim
    elif c == "down":
        aim += int(n)
    else:
        aim -= int(n)

print(pos*depth)
