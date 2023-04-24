with open('ruchy.txt') as dane, open('wynik3.txt', 'w') as wynik:
    dane = dane.readline().rstrip()
    ruchy = []
    for x in range(50):
        r = dane[x * 50:x * 50 + 50:1]
        temp = [y for y in r]
        ruchy.append(temp)

    for x in ruchy:
        print(x)


    def najdluzszy_podciag_tych_samych_liter(lista):
        max_dlugosc = 0
        dlugosc = 1
        for i in range(1, len(lista)):
            if lista[i] == lista[i - 1]:
                dlugosc += 1
            else:
                dlugosc = 1
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
        return max_dlugosc


    def a():
        r = []
        for x in ruchy:
            r.append(najdluzszy_podciag_tych_samych_liter(x))
        print(f'|Zadanie 3.2\nNajdłuższy spójny ciąg to {max(r)}', file=wynik)


    def b():
        plansza = [
            "#..",
            "#..",
            "###"
        ]
        x, y = 1, 1
        max_x, max_y = 3, 3
        for polecenie in dane  :
            if polecenie == "N" and y==1:
                    y = y + 1
            if polecenie == "S" and y==2:
                    y = y - 1
            if polecenie == "E" and x == 1:
                    x = x + 1
            if polecenie == "W" and x==2:
                    x = x - 1
        print(f"Zadanie 3.3\nWwpółrzędne to ({x},{y})", file=wynik)

    a()
    b()
    # print(najdluzszy_podciag_tych_samych_liter(["a","b","b","b"]))
