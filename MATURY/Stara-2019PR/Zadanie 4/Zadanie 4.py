with open('dzialki.txt') as dzialki, open('przyklad.txt') as przyklad,open('wynik4.txt', 'w') as wyniki:
    dane = dzialki
    # dane = przyklad
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip(), dane))

    # Import danych
    amount = (len(dane)+1)//31
    dzialki = []
    for x in range(amount):
        dzialka = []
        start = x*31
        stop = 30 + 31*x
        for y in range(start,stop):
            dzialka.append(dane[y])
        dzialki.append(dzialka)

    """
    . - puste
    * - trawa
    X - przeszkoda
    
    """
    def a():
        count = 0
        for dzialka in dzialki:
            pola = 30*30
            ile_trawy = 0
            for wiersz in dzialka:
                ile_trawy += wiersz.count("*")
            count += (ile_trawy/pola) >= 0.7
        print(f"Zadanie 4.1\nDziałek porośniętych trawą w conajmniej 70% jest {count}",file=wyniki)

    def flip(arr):
        new_arr = []
        for x in arr[::-1]:
            new_arr.append(x[::-1])
        return new_arr
    def b():
        dzialki_180 = []
        for dzialka in dzialki:
            dzialki_180.append(flip(dzialka))

        result = []
        for x in range(len(dzialki)):
            for y in range(len(dzialki)):
                if dzialki[x] == dzialki_180[y]:
                    result.append(",".join(list(map(str,sorted([x+1,y+1])))))
        print(f"\nZadanie 4.2\nTakie pary działek to {' i '.join(list(set(result)))}",file=wyniki)

    def czy_pusty(dzialka,wymiar):
        kwadrat = ""
        for x in range(wymiar+1):
            kwadrat += dzialka[x][0:wymiar+1]
        if "X" in kwadrat:
            return False
        return True
    def c():
        numer, kwadrat = [],-1
        for z in range(len(dzialki)):
            dzialka = dzialki[z]
            wymiar = 0
            czy_kwadrat_pusty = True
            while czy_kwadrat_pusty:
                wymiar +=1
                czy_kwadrat_pusty = czy_pusty(dzialka,wymiar)
            if wymiar > kwadrat:
                kwadrat = wymiar
                numer.clear()
                numer.append(z+1)
            elif wymiar == kwadrat:
                numer.append(z+1)
        print(f"Zadanie 4.3\nNajwiększy kwadrat jest na dzialkach o numerach {' '.join(list(map(str,numer)))} o boku {kwadrat}",file=wyniki)

    a()
    b()
    c()