with open('galerie.txt') as galerie, open('galerie_przyklad.txt') as przyklad:
    dane = galerie
    # dane = przyklad
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip().split(), dane))

    nowe = []

    for x in dane:
        temp = []
        temp.append(x[0])
        temp.append(x[1])
        temp.append([int(y)for y in x[2::] if y != '0'])
        nowe.append(temp)

    print(nowe)
    def a():
        miasta = {}
        for x in nowe:
            if x[0] in miasta:
                miasta[x[0]] +=1
            else:
                miasta[x[0]] = 1
        for x,y in miasta.items():
            print(x,y)

    def b():
        max_powierzcnia,max_miasto = 0,""
        min_powierzchnia, min_miasrto = 1000000,""
        for x in nowe:
            miasto = x[1]
            lokale = x[2]
            liczba_lokali = len(lokale) // 2
            powierzchnia = 0
            for y in range(0,len(lokale),2):
                powierzchnia += lokale[y] * lokale[y+1]

            if powierzchnia > max_powierzcnia:
                max_powierzcnia = powierzchnia
                max_miasto = miasto
            if powierzchnia < min_powierzchnia:
                min_powierzchnia = powierzchnia
                min_miasrto = miasto

            print(miasto, powierzchnia, liczba_lokali)
        print()
        print(max_miasto,max_powierzcnia)
        print(min_miasrto,min_powierzchnia)


    def c():
        max_loakle, max_miasto = 0,""
        min_lokale, min_miasto = 100000,""
        for x in nowe:
            miasto = x[1]
            lokale = x[2]
            powierzchnie = []
            for y in range(0, len(lokale),2):
                powierzchnie.append(lokale[y]*lokale[y+1])
            ilosc = len(set(powierzchnie))
            if ilosc > max_loakle:
                max_loakle = ilosc
                max_miasto = miasto
            if ilosc < min_lokale:
                min_lokale = ilosc
                min_miasto = miasto
        print()
        print(max_miasto,max_loakle)
        print(min_miasto,min_lokale)
    a()
    b()
    c()