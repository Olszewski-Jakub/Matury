with open('dane_geny.txt') as dane, open('wyniki_gen.txt', 'w') as wyniki:
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip(), dane))


    # print(dane)

    def a():
        slow = {}
        for x in dane:
            if len(x) not in slow:
                slow[len(x)] = 1
            else:
                slow[len(x)] += 1
        print(f"69.1\nLiczba gatunkow: {len(slow)}\nliczba osobnikow: {max(slow.values())}\n", file=wyniki)




    geny = []
    geny_odwr = []


    for x in dane:
        temp = []
        pocz = -1
        czy_w_genie = False
        for y in range(len(x) - 1):
            if x[y] + x[y + 1] == 'AA' and not czy_w_genie:
                pocz = y
                czy_w_genie = True
            if x[y] + x[y + 1] == 'BB' and czy_w_genie:
                temp.append(x[pocz:y + 2])
                czy_w_genie = False
        # print(x, temp)
        geny.append(temp)

    for x in dane:
        x = x[::-1]
        temp = []
        pocz = -1
        czy_w_genie = False
        for y in range(len(x) - 1):
            if x[y] + x[y + 1] == 'AA' and not czy_w_genie:
                pocz = y
                czy_w_genie = True
            if x[y] + x[y + 1] == 'BB' and czy_w_genie:
                temp.append(x[pocz:y + 2])
                czy_w_genie = False
        # print(x, temp)
        geny_odwr.append(temp)

    def sprawdz(x):
        for y in x:
            if 'BCDDC' in y:
                return True
        return False


    def b():
        c = 0
        for x in geny:
            if sprawdz(x):
                c += 1
        print(f"69.2\nIlosc osobnikow: {c}", file=wyniki)


    def c():
        m = 0
        m_genu = 0
        for x in geny:
            m = max(m, len(x))
            for y in x:
                m_genu = max(len(y), m_genu)

        print(m, m_genu)

    def d():
        odporny, silnie_odporny = 0,0
        for x in dane:
            if x == x[::-1]:
                silnie_odporny += 1
        for x in range(len(geny)):
            if geny[x] == geny_odwr[x]:
                odporny += 1
        print(odporny,silnie_odporny)


    a()
    b()
    c()
    d()