def compare(a, b):
    i = 0
        
    while True:
        if len(a) == i and len(b) != i:
            return True
        elif len(b) == i and len(a) != i:
            return False
        elif len(a) == i and len(b) == i:
            return None
        if type(a[i]) == int and type(b[i]) == int:
            if a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
        else:
            one = a[i]
            two = b[i]
            if type(one) != list:
                one = [one]
            elif type(two) != list:
                two = [two]

            if compare(one, two) != None:
                return compare(one, two) 
        i += 1








def p1(f):
    data = f.read().split("\n\n")
    c = 0
    for idx, pair in enumerate(data):
        a, b = pair.split("\n")
        l_1 = eval(a)
        l_2 = eval(b)

        if compare(l_1, l_2):
            c += idx + 1
    return c

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare
from functools import cmp_to_key

def p2(f):
    data = f.read().split("\n")
    data.append("[[2]]")
    data.append("[[6]]")

    new_data = []
    for i in data:
        if i:
            new_data.append(eval(i))

    new = sorted(new_data, key=cmp_to_key(make_comparator(compare)))
    return (new.index([[2]])+1) * (new.index([[6]]) + 1)

print(p2(open("2022/p13/input_sample.txt")))
    