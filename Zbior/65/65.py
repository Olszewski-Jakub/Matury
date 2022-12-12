with open('dane_ulamki.txt') as dane, open("wyniki_ulamki.txt", 'w') as wyniki:
    dane = dane.readlines()
    dane = list(map(lambda x: list(map(lambda y: int(y), x.rstrip().split())), dane))


    def do_nieskrac(a, b):
        return b // nwd(a, b)


    def nwd(a, b):
        while b:
            a, b = b, a % b
        return a


    def a():
        min = float("inf")
        licz = 0
        mian = 0
        for x in dane:
            if min < (n := (x[0] / x[1])):
                pass
            if min > (n := (x[0] / x[1])):
                min = n
                licz = x[0]
                mian = x[1]
            elif min == (x[0] / x[1]) and mian > (n := x[1]):
                mian = n
                licz = x[0]
        print("Zadanie 1:", licz, mian, file=wyniki)


    def b():
        count = 0
        for x in dane:
            if nwd(x[1], x[0]) == 1:
                count += 1
        print("Zadanie 2:", count, file=wyniki)


    def c():
        sum = 0
        for x in dane:
            if nwd(x[1], x[0]) == 1:
                sum += x[1]
            else:
                sum += do_nieskrac(x[0], x[1])
        print("Zadanie 3:", sum, file=wyniki)

    def d():
        i, mianS, liczS, nowyLicz = 0, 2 * 3 * 5 * 7 * 13, 0, 0

        mianS = mianS * mianS / 13
        for x in dane:
            nowyLicz = x[0] * mianS / x[1]
            liczS += nowyLicz

        print("Zadanie 4: ", liczS,file=wyniki)


    a()
    b()
    c()
    d()