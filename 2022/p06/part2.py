with open("input.txt") as f:
    data = f.read()
import sys
for i in range(13, len(data)):
    l = []
    for j in range(14):
        l.append(data[i-j])

    s = set(l)


    if len(s) == 14:

        print(i+1)
        sys.exit(0)


    
