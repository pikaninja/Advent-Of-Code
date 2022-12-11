import json
def p1(f):
    data = f.read().split("\n\n")
    size = len(data)
    monkeys = [{} for i in range(size)]

    for idx, monk in enumerate(data):
        monk = monk.split("\n")
        items = monk[1].strip("Starting items: ")
        items = list(map(int, items.split(", ")))
        monkeys[idx]["items"] = items
        operation = monk[2].split(" ")[-2]
        thing = monk[2].split(" ")[-1]
        monkeys[idx]["op"] = [operation, thing]
        monkeys[idx]["d"] = int(monk[3].split()[-1])
        monkeys[idx]["t"] = int(monk[4].split()[-1])

        monkeys[idx]["f"] = int(monk[5].split()[-1])
    inspect = {i:0 for i in range(size)}
    def run_monk(idx):
        for i in monkeys[idx]["items"]:
            worry = i
            if monkeys[idx]["op"][0] == "*":
                if monkeys[idx]["op"][1] == "old":
                    worry *= worry
                else:
                    worry *= int(monkeys[idx]["op"][1])
            elif monkeys[idx]["op"][0] == "+":
                if monkeys[idx]["op"][1] == "old":
                    worry += worry
                else:
                    worry += int(monkeys[idx]["op"][1])
            worry = worry // 3

            if worry % monkeys[idx]["d"] == 0:
                monkeys[monkeys[idx]["t"]]["items"].append(worry)
            else:
                monkeys[monkeys[idx]["f"]]["items"].append(worry)
            inspect[idx] += 1

        monkeys[idx]["items"] = []



    for _ in range(20):
        for i in range(size):
            run_monk(i)

    d = list(inspect.values())

    d.sort()
    return d[-1] * d[-2]
        






def p2(f):
    data = f.read().split("\n\n")

    size = len(data)
    monkeys = [{} for i in range(size)]
    su = 1
    for idx, monk in enumerate(data):
        monk = monk.split("\n")
        items = monk[1].strip("Starting items: ")
        items = list(map(int, items.split(", ")))
        monkeys[idx]["items"] = items
        operation = monk[2].split(" ")[-2]
        thing = monk[2].split(" ")[-1]
        monkeys[idx]["op"] = [operation, thing]
        monkeys[idx]["d"] = int(monk[3].split()[-1])
        su *= monkeys[idx]["d"]
        monkeys[idx]["t"] = int(monk[4].split()[-1])

        monkeys[idx]["f"] = int(monk[5].split()[-1])
    inspect = {i:0 for i in range(size)}
    def run_monk(idx):
        for i in monkeys[idx]["items"]:
            worry = i
            if monkeys[idx]["op"][0] == "*":
                if monkeys[idx]["op"][1] == "old":
                    worry *= worry
                else:
                    worry *= int(monkeys[idx]["op"][1])
            elif monkeys[idx]["op"][0] == "+":
                if monkeys[idx]["op"][1] == "old":
                    worry += worry
                else:
                    worry += int(monkeys[idx]["op"][1])

            if worry % monkeys[idx]["d"] == 0:
                monkeys[monkeys[idx]["t"]]["items"].append(worry%su)
            else:
                monkeys[monkeys[idx]["f"]]["items"].append(worry%su)
            inspect[idx] += 1

        monkeys[idx]["items"] = []



    for _ in range(10000):
        for i in range(size):
            run_monk(i)


    d = list(inspect.values())

    d.sort()
    return d[-1] * d[-2]

        
