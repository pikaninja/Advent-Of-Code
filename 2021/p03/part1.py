with open("input.txt") as f:
    data = f.read().splitlines()

value1 = [0 for i in range(len(data[0]))]
value2 = [0 for i in range(len(data[0]))]

for bin in data:
    for idx, c in enumerate(bin):
        if c == "1":
            value1[idx] += 1
        else:
            value2[idx] += 1

gamma, epsilon = "", ""
for i in range(len(data[0])):
    if value1[i] > value2[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma,2) * int(epsilon, 2))


