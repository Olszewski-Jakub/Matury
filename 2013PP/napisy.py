with open('napisy.txt') as napisy:
    napisy = napisy.readlines()
    napisy = list(map(lambda x: x.rstrip(), napisy))
    # print(napisy)

    # a)
    c = 0
    for x in napisy:
        if len(x)%2 == 0:
            c+=1
    print(c)

    # b)
    c=0
    for x in napisy:
        if x.count('1') == x.count('0'):
            c+=1

    print(c)

    # c)
    c_zero, c_jeden = 0,0
    for x in napisy:
        if x.count('0') == 0:
            c_jeden+=1
        elif x.count('1') == 0:
            c_zero+=1
    print(f"same 0 {c_zero}, same 1 {c_jeden}")

    # d)
    slownik = {}
    for x in napisy:
        l = len(x)
        if l in slownik.keys():
           slownik[l] +=1
        else:
            slownik[l] = 1
    for x in range(2,17):
        print(f"{x} znaki {slownik.get(x)}")