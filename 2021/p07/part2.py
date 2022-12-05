with open("input.txt") as f:
    data = list(map(int, f.read().split(",")))

l = 0
r = max(data)

def count(pos):
    c = 0
    for i in data:
        n = abs(i-pos)
        c += n * (n+1)/2
    return c

mini = 99999999
for i in range(max(data)+1):
    mini = min([mini, count(i)])

print(mini)
