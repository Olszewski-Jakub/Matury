with open('dane.txt') as dane, open('przyklad.txt') as przyklad, open('wyniki6.txt', "w") as wyniki:
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip(), dane))
    przyklad = przyklad.readlines()
    przyklad = list(map(lambda x: x.rstrip(), przyklad))

    r = dane

    obrazek = []
    for x in r:
        obrazek.append(list(map(int, x.split())))


    def a():
        jasny, ciemny = 0, 255
        for i in obrazek:
            jasny = max(i + [jasny])
            ciemny = min(i + [ciemny])
        print(f"6.1 jasny {jasny} ciemny {ciemny}", file=wyniki)


    def b():
        c = 0

        for i in obrazek:
            if not i == i[::-1]:
                c += 1

        print(c)


    def c():
        # Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128
        c = 0
        for i in range(320):
            for j in range(200):
                czy_zachodzi = False
                for wiersz, kolumna in [(j + 1, i), (j, i + 1), (j - 1, i), (j, i - 1)]:
                    if 0 <= wiersz < 200 and 0 <= kolumna < 320:
                        if abs(obrazek[j][i] - obrazek[wiersz][kolumna]) > 128:
                            czy_zachodzi = True
                if czy_zachodzi:
                    c += 1
        print(c)


    def d():
        max_ciag = 0
        for kolumna in range(320):
            ciag = 0
            el = obrazek[0][kolumna]
            for wiersz in range(199):
                if el == obrazek[wiersz][kolumna]:
                    ciag +=1
                    max_ciag = max(max_ciag, ciag)
                else:
                    el = obrazek[wiersz][kolumna]
                    ciag = 1

                # if obrazek[wiersz][kolumna] == obrazek[wiersz + 1][kolumna]:
                #     ciag += 1
                #     if wiersz == 198:
                #         ciag += 1
                #     max_ciag = max(ciag, max_ciag)
                #
                # else:
                #     ciag = 2

        print(max_ciag)


    a()
    b()
    c()
    d()
