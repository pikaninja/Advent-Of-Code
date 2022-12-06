with open("input.txt") as f:
    data = f.read()
import sys
for i in range(3, len(data)):
    s = set([data[i], data[i-1], data[i-2], data[i-3]])

    print(s)

    if len(s) == 4:

        print(i+1)
        sys.exit()


    
