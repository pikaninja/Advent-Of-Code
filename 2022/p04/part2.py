with open("input.txt") as f:
    data = f.read().splitlines()


count = 0
for row in data:
    a, b = row.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)




    if a1 <= b1 and a2 >= b1:
        count += 1
    elif b1 <= a1 and b2 >= a1:
        count += 1
    elif a1 <= b1 and a2 >= b2:
        print("a", a1, a2, b1, b2)
        count += 1
    elif b1 <= a1 and b2 >= a2:

        print("b", a1, a2, b1, b2)
        count += 1

print(count)
