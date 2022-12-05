fish = dict()
days = 80
with open("input.txt","r") as inputfile:
    counters = [ int(x) for x in inputfile.read().strip().split(',') ]
for i in range(9):
    fish[i] = counters.count(i)
for i in range(days):
    fish[(i+7)%9] += fish[i%9]
print(sum(fish.values()))
days = 256
for i in range(80,days):
    fish[(i+7)%9] += fish[i%9]
print(sum(fish.values()))
