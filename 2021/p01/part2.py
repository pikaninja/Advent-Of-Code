with open("input.txt") as f:
    data = list(map(int, f.read().splitlines()))

sum = data[0] + data[1] + data[2]

c = 0

for i in range(3, len(data)):
    oldsum = sum
    sum -= data[i-3]
    sum += data[i]

    if sum > oldsum:
        c += 1
print(c)
