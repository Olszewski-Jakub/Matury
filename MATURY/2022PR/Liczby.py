with open('liczby.txt') as liczby, open('przyklad.txt') as przyklad:
    dane = liczby
    # dane = przyklad
    dane = dane.readlines()
    dane = list(map(lambda x: int(x.rstrip()), dane))


    # print(dane)

    def a():
        first = ""
        count = 0
        for x in dane:
            x = str(x)
            if x[0] == x[-1]:
                if count == 0:
                    first = x
                count += 1
        print(count, first)


    def rozklad(n):
        czynniki = []
        k = 2
        while n != 1:
            while n % k == 0:
                n //= k
                czynniki.append(k)
            k += 1
        return czynniki


    def b():
        czynniki_max = [0, 0]
        rozne_czynniki_max = [0, 0]
        for x in dane:
            czynniki = rozklad(x)
            ilosc_czynnikow = len(czynniki)
            rozne_czynniki = len(set(czynniki))

            if czynniki_max[1] < ilosc_czynnikow:
                czynniki_max[0] = x
                czynniki_max[1] = ilosc_czynnikow

            if rozne_czynniki_max[1] < rozne_czynniki:
                rozne_czynniki_max[0] = x
                rozne_czynniki_max[1] = rozne_czynniki

        print(czynniki_max[0], czynniki_max[1], rozne_czynniki_max[0], rozne_czynniki_max[1])


    def dobre_trojki(x, y, z):
        return (y % x == 0 and z % y == 0)


    def c():
        count = 0
        count2 = 0
        trojki = []
        for x in dane:
            for y in dane:
                for z in dane:
                    if len(set([x, y, z])) == 3:
                        if dobre_trojki(x, y, z):
                            count += 1
                            trojki.append([x, y, z])
                            for a in dane:
                                for b in dane:
                                    if len(set([x, y, z, a, b])) == 5:
                                        if dobre_trojki(z, a, b):
                                            count2 += 1

        print(count, "\n")
        for x in trojki:
            print(*x)
        print()
        print(count2, "\n")


    a()
    b()
    c()
