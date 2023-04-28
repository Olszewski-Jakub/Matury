with open('wykreslanka.txt') as wykreslanka:
    wykreslanka = wykreslanka.readlines()
    wykreslanka = list(map(lambda x: x.rstrip(), wykreslanka))
    # print(wykreslanka)

    def a():
        wiersze = []
        for x in range(len(wykreslanka)):
            if 'matura' in wykreslanka[x]:
                wiersze.append(x)
        kolumny = []
        for k in range(200):
            kolumna_temp = ""
            for w in range(100):
                kolumna_temp += wykreslanka[w][k]
            if 'matura' in kolumna_temp:
                kolumny.append(k)

        print('Kolumny: ', *kolumny)
        print('wiersze: ', *wiersze)

    def b():
        wiersze = []
        for x in wykreslanka:
            max_dl = 0
            temp = x[0]
            dl = 1
            for y in range(1,200):
                if x[y] == temp:
                    dl += 1
                    max_dl = max(dl,max_dl)
                else:
                    dl=1
                    temp = x[y]
            wiersze.append(max_dl)
        maxmax_dl = max(wiersze)
        r = wiersze.index(maxmax_dl)
        # print(r)
        for index,x in enumerate(wiersze):
            if x == maxmax_dl:
                print(index, x)
    from string import ascii_lowercase
    def czy_wszystkie_litery(s):
        letters = [0] * 26
        for x in s:
            letters[ord(x) -ord('a')] += 1

        return letters.count(1) == 26






    # a()
    # b()
    c()
    print(czy_wszystkie_litery(ascii_lowercase))
