with open("input.txt") as f:
    data = f.read()

lists = [[] for i in range(9)]

data = data.split("\n\n")

crates = data[0].splitlines()
steps = data[1].splitlines()
crates.pop()
for i in crates[::-1]:
    count = 0
    for j in range(1, 4*9-1, 4):
        print(i[j])
        if i[j] != " ":
            lists[count].append(i[j])
        count += 1

print(lists)
for i in steps:
    print(i)
    a, b = i.split(" from ")
    num = int(a.strip().split(" ")[-1])
    start = int(b.strip()[0].strip())-1
    end = int(b.strip()[-1].strip())-1

    new = []
    for i in range(num):
            top = lists[start][-1]
            lists[start].pop()
            new.append(top)

    new = new[::-1]
    lists[end] += new

    print(lists)


out = ""
for i in lists:
    print(i)
    if i:
        out += i[-1]
print(out)

