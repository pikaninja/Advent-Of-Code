with open ("input.txt") as f:

    aghList = []

    arghhh = []

    aidsInput = f.read()

    damnYouAOC = [["J", "Z", "G", "V", "T", "D", "B", "N"], ["F", "P", "W", "D", "M", "R", "S"], ["Z", "S", "R", "C", "V"], ["G", "H", "P", "Z", "J", "T", "R"], ["F", "Q", "Z", "D", "N", "J", "C", "T"], ["Q", "P", "B", "V", "C", "G"], ["N", "P", "B", "Z"], ["J", "P", "W"]]

    instructions = aidsInput.split("\n")

    #print(instructions)

    argh = [s.strip(' move ') for s in instructions]

    #print(ARGH)

    print(argh)

    arghh = [s.split(' from ') for s in argh]

    #print(ARGHH)

    for i in arghh:
        print(i)
        bruh = i.split(" to ")
        arghhh.append(bruh)

    #ARGHHH = [s.strip(' to ') for s in arghh]

    print(arghhh)

    # for i in instructions:
    #     a = i.split("move", "from")


    #     aghList.append(a)

    #print(aghList)
