with open("input.txt") as f:
    data = f.read().splitlines()

def most_common_bit(d, idx):

    one, zero = 0, 0
    for num in d:
        bit = int(num[idx]) 
        if bit == 1:
            one += 1
        else:
            zero += 1


    return 1 if one >= zero else 0


def filter_out(d, idx, bit):
    new_d = []

    for num in d:
        if int(num[idx]) == bit:
            new_d.append(num)
    return new_d


oxy_list = data[::]
co2_list = data[::]

for i in range(len(data[0])):

    bit = most_common_bit(oxy_list, i)
    oxy_list = filter_out(oxy_list, i, bit)


    if len(co2_list) > 1:
        bit = most_common_bit(co2_list, i)
        bit = 1 - bit
    
        print(bit, co2_list, i)
        co2_list = filter_out(co2_list, i, bit)


        

print(int(co2_list[0],2) * int(oxy_list[0], 2))


