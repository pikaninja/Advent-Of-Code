with open("input.txt") as f:
    data = f.read().splitlines()

priority = 0

alpha = "abcdefghijklmnopqrstuvwxyz"
count = 0
mp = {}
for row in data:

    s = set()
    for i in row:
        s.add(i)

    for i in list(s):
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    count += 1

    if count == 3:
        print(mp)
        for i in mp:
            print(mp[i])
            if mp[i] == 3:
                print("1")
                if i in alpha:
                    priority += ord(i) - ord("a") + 1
                else:
                    priority += ord(i) - ord("A") + 27
                break

        mp = {}
        count = 0

print(priority)





