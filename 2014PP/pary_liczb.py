def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

def suma_cyfr(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

with open("PARY_LICZB.TXT") as pary_x:
    pary_x = pary_x.readlines()
    pary_x = list(map(lambda x: x.rstrip(), pary_x))
    pary = []
    for x in pary_x:
        pary.append(list(map(int,x.split(" "))))
    # print(pary)

    # a)
    c = 0
    for x in pary:
        if x[0] % x[1] == 0:
            c+=1

        elif x[1] % x[0] == 0:
            c+=1

    print(c)

    # b)
    c = 0
    for x in pary:
        if nwd(x[0],x[1]) == 1:
            c+=1
    print(c)

    # c)
    c=0
    for x in pary:
        if suma_cyfr(x[0]) == suma_cyfr(x[1]):
            c+=1
    print(c)