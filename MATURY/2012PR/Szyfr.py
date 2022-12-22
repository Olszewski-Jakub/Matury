with open('klucze1.txt') as klucze1, open('klucze2.txt') as klucze2, open('sz.txt') as sz, open('tj.txt') as tj:
    klucze1 = klucze1.readlines()
    klucze1 = list(map(lambda x: x.rstrip(), klucze1))
    klucze2 = klucze2.readlines()
    klucze2 = list(map(lambda x: x.rstrip(), klucze2))
    sz = sz.readlines()
    sz = list(map(lambda x: x.rstrip(), sz))
    tj = tj.readlines()
    tj = list(map(lambda x: x.rstrip(), tj))

    for a in range(len(tj)):
        x = tj[a]
        y = klucze1[a]
        wynik=""
        for i in range(len(x)):
            temp = ord(x[i])+ord(y[i % len(y)])-64
            if temp > 90:
                temp -= 26
            wynik += chr(temp)
        print(wynik)

    print()
    print()
    print()
    for a in range(len(sz)):
        x = sz[a]
        y = klucze2[a]
        wynik = ""
        for i in range(len(x)):
            temp = ord(x[i]) - ord(y[i % len(y)]) + 64
            if temp < 65:
                temp += 26
            wynik += chr(temp)
        print(wynik)