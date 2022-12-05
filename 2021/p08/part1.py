with open("input.txt") as f:
    data = f.read().splitlines()

count = 0

for row in data:
    output = row.split(" | ")[1].split(" ")

    for out in output:
        if len(out) in [2, 3, 4, 7]:
            print(out)
            count += 1

print(count)
