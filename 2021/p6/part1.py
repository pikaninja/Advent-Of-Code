with open("input.txt") as f:
    data = list(map(int, f.read().split(",")))

for i in range(80):
    for i in range(len(data)):
        if data[i] > 0:
            data[i] -= 1
        else:
            data[i] = 6
            data.append(8)
print(len(data))
