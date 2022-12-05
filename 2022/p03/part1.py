with open("input.txt") as f:
    data = f.read().splitlines()

priority = 0

alpha = "abcdefghijklmnopqrstuvwxyz"
for row in data:
    a = row[len(row)//2:]
    b = row[:len(row)//2]
    print(a, b)

    mp = {}

    for i in a:
        mp[i] = 1

    for i in b:
        if i in mp.keys():
            print(i)
            if i in alpha:
                priority += ord(i) - ord("a") + 1
            else:
                priority += ord(i) - ord("A") + 27
            break
print(priority)





