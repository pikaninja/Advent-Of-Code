with open("input.txt") as f:
    data = list(map(int, f.read().splitlines()))

c = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        c += 1

print(c)

