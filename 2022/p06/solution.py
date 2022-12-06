def p1(f):
    data = f.read()
    for i in range(3, len(data)):
        s = set(data[i-4:i])
    
        if len(s) == 4:
    
            return i

def p2(f):
    data = f.read()
    for i in range(13, len(data)):
        s = set(data[i-14:i])


        if len(s) == 14:
            return i




