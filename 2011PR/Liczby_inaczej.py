with open('liczby.txt') as liczby:
    liczby = liczby.readlines()
    liczby = list(map(lambda x: x.rstrip(), liczby))
    # print(liczby)

    # a)
    # system 2-owy
    c = 0
    for x in liczby:
        if x[-1] == '0':
            c += 1
    print(c)

    # b)
    # bin()
    # oct()
    # hex()
    l = list(map(lambda x: int(x, 2), liczby))
    print(max(l), bin(max(l)).lstrip("0b"))
    # print(max(l),bin(max(l))[2:])


    #c)
    sum = 0
    for x in liczby:
        if len(x) == 9:
            sum += int(x,2)

    print(bin(sum).lstrip("0b"))

