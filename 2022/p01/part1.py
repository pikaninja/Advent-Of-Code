with open("input.txt") as f:
    data = f.read().split("\n\n")

maxi = 0


for i in data:
    sumi = 0
    for j in i.split("\n"):
        if j:
            sumi += int(j)
    maxi = max([sumi, maxi])


print(maxi)


