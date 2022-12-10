def p1(f):
    data = f.read().splitlines()
    signal = 1
    add = {}
    total = 0
    i = 1
    for command in data:
        if command == "noop":
            i += 1
            if (i+ 20) % 40 == 0:
                total += signal * i
            continue
        else:
            i += 1
            if (i+ 20) % 40 == 0:
                total += signal * i
            a = int(command.split()[1])
            signal += a
            i += 1

        if (i+ 20) % 40 == 0:
            total += signal * i


    return total

def p2(f):
    data = f.read().splitlines()
    signal = 1
    add = {}
    total = 0
    i = 1
    arr = ["" for i in range(7)]
    arr[0] += "#" # idfk why this isn't added by hey i could read the characters without it so
    for command in data:
        if command == "noop":
            if abs(signal - (i%40)) <= 1:
                arr[i//40]+="#"
            else:
                arr[i//40]+="."

            i += 1
            continue
        else:
            if abs(signal - (i%40)) <= 1:
                arr[i//40]+="#"
            else:
                arr[i//40]+="."
            i += 1
     
            a = int(command.split()[1])
            signal += a
            if abs(signal - (i%40)) <= 1:
                arr[i//40]+="#"
            else:
                arr[i//40]+="."
            i += 1
    return "\n".join(arr)

