with open('szachy.txt') as szachy, open('szachy_przyklad.txt') as szachy_p:
    # TODO zmienic dane
    dane, lw = szachy, 125
    # dane, lw = szachy_p, 9

    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip(), dane))
    szachownice = []
    # 0 -7
    # 9 - 16
    for x in range(0, lw, 1):
        temp = []
        for y in range(8):
            index = 9 * x + y
            temp.append(dane[index])
        szachownice.append(temp)


    # print(szachownice)

    def a1(szachownica):
        pusta = 0
        for x in range(8):
            temp = 0
            for y in range(8):
                if szachownica[y][x] == '.':
                    temp += 1
            if temp == 8:
                pusta += 1
        return pusta


    def a():
        count = 0
        max_pusta = 0
        for x in szachownice:
            if (z := a1(x)) > 0:
                count += 1
                max_pusta = max(max_pusta, z)

        print(count, max_pusta)


    def b():
        count = 0
        najmniej_figur = 64
        for szachownica in szachownice:
            lista_figur = {}
            for wiersz in szachownica:
                for figura in wiersz:
                    if figura != ".":
                        if figura.lower() in lista_figur:
                            if figura.isupper():
                                lista_figur[figura.lower()] += 1
                            else:
                                lista_figur[figura] -= 1
                        else:
                            if figura.isupper():
                                lista_figur[figura.lower()] = 1
                            else:
                                lista_figur[figura] = -1

            if sum(lista_figur.values()) == 0:
                count += 1
                kropki = 0
                pola = 8*8
                for wiersz in szachownica:
                    kropki += wiersz.count('.')

                figura = pola - kropki
                najmniej_figur = min(figura, najmniej_figur)


        print(count, najmniej_figur)

    def isCheck(linia, k_index, w_index):
        odleglosc = int(abs(k_index-w_index))
        if k_index> w_index:
            if linia[w_index+1: k_index].count('.') == odleglosc-1:
                return True
        else:
            if linia[int(k_index)+1: int(w_index)].count('.') == odleglosc-1:
                return True
        return False


    def c():
        # [Biały szach, czarny szach]
        figury = [['W', 'k'], ['K','w']]
        result = [0,0]
        for szachownica in szachownice:
            for przypadki in range(2):
                for wiersz in szachownica:
                    if figury[przypadki][0] in wiersz and figury[przypadki][1] in wiersz:
                        W_index, k_Index = wiersz.index(figury[przypadki][0]), wiersz.index(figury[przypadki][1])
                        result[przypadki] += isCheck(wiersz,k_Index,W_index)

                for kolumna in range(8):
                    linia = ""
                    for wiersz in range(8):
                        linia += szachownica[wiersz][kolumna]

                    if figury[przypadki][0] in linia and figury[przypadki][1] in linia:
                        W_index, k_Index = linia.index(figury[przypadki][0]), linia.index(figury[przypadki][1])
                        result[przypadki] += isCheck(linia,k_Index,W_index)

        print(*result)



    a()
    b()
    c()
