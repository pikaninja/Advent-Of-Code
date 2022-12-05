print(max([sum([int(num) for num in line.split("\n") if num]) for line in open("input.txt").read().split("\n\n")]))
